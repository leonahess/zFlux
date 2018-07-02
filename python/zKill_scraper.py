import requests
import datetime
import logging
import time
import csv
from influxdb import InfluxDBClient


def EsiCall(ids):
    retry_time = 1
    while retry_time < 5:
        v = requests.post('https://esi.tech.ccp.is/latest/universe/names/?&datasource=tranquility', json=ids)
        if v.status_code == 200:
            break
        logger.warning("Esi call failed")
        time.sleep(2 ^ retry_time)
        retry_time = retry_time + 1

    if v.status_code == 200:
        try:
            names = v.json()
        except ValueError as e:
            logger.warning("esi json decode has failed!: {}".format(e))
    else:
        names = []

    return names


def FetchVictimNameWithId(killmail):

    victim_ids = []

    if 'character_id' in killmail['package']['killmail']['victim']:
        victim_ids.append(killmail['package']['killmail']['victim']['character_id'])

    if 'corporation_id' in killmail['package']['killmail']['victim']:
        victim_ids.append(killmail['package']['killmail']['victim']['corporation_id'])

    if 'alliance_id' in killmail['package']['killmail']['victim']:
        victim_ids.append(killmail['package']['killmail']['victim']['alliance_id'])

    names = EsiCall(victim_ids)

    logger.debug("Victim ids: {}".format(victim_ids))
    logger.debug("Victim names: {}".format(names))

    return names


def FetchAttackerNameWithId(killmail):

    attacker_ids = []

    for entry in killmail['package']['killmail']['attackers']:
        if 'character_id' in entry and entry['character_id'] not in attacker_ids:
            attacker_ids.append(entry['character_id'])
        if 'corporation_id' in entry and entry['corporation_id'] not in attacker_ids:
            attacker_ids.append(entry['corporation_id'])
        if 'alliance_id' in entry and entry['alliance_id'] not in attacker_ids:
            attacker_ids.append(entry['alliance_id'])

    names = EsiCall(attacker_ids)

    logger.debug("Attacker attacker_ids: {}".format(attacker_ids))
    logger.debug("Attacker names: {}".format(names))

    return names


def GetAttackerShips(dict):
    attacker_ship_list = []
    attacker_ship_name_list = []
    attacker_ship_name_str = ''

    for x in range(0, len(dict['package']['killmail']['attackers'])):
        try:
            if dict['package']['killmail']['attackers'][x]['ship_type_id'] not in attacker_ship_list:
                attacker_ship_list.append(dict['package']['killmail']['attackers'][x]['ship_type_id'])
        except KeyError:
            logger.error("attacker ship key error")
    logger.debug("attacker_ship_list: {}".format(attacker_ship_list))

    with open('invTypes.csv', newline='') as f:
        inv_types = csv.reader(f)
        for row in inv_types:
            for l in range(0, len(attacker_ship_list)):
                if row[0] == str(attacker_ship_list[l]):
                    attacker_ship_name_list.append(row[2])
    logger.debug("Ship name list: {}".format(attacker_ship_name_list))

    for k in range(0, len(attacker_ship_name_list)):
        attacker_ship_name_str = attacker_ship_name_str + ';' + attacker_ship_name_list[k]
    attacker_ship_name_str = attacker_ship_name_str + ';'
    logger.debug("attacker_ships: {}".format(attacker_ship_name_str))

    return attacker_ship_name_str


start = datetime.datetime.now()
last100_processing_time = []
counter = 1


# start logger
logging.basicConfig(filename='zKill_scraper_{}.log'.format(start), level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

# Connect to Database and check if database 'eve' exists, otherwise create one
client = InfluxDBClient(host='localhost', port=8086, database='eve')
database_list = client.get_list_database()
eve_exists = False
for s in range(0, len(database_list)):
    if database_list[s]['name'] == 'eve':
        eve_exists = True
if not eve_exists:
    client.create_database('eve')

while True:
    try:
        r = requests.get('https://redisq.zkillboard.com/listen.php?queueID=zKill_scaperDev', timeout=20)
    except requests.exceptions.Timeout:
        logger.warning("zKill request timed out")
    except requests.exceptions.RequestException as e:
        logger.error("zKill requests had a exception: {}".format(e))
    try:
        dict = r.json()
    except ValueError as e:
        logger.warning("redisQ json decode has failed!: {}".format(e))

    then = datetime.datetime.now()

    if r.text == '{"package":null}':
        logger.info(r.text)

    if dict['package'] is not None:

        # METADATA
        killID = dict['package']['killID']
        killmail_time = dict['package']['killmail']['killmail_time']
        solar_systemID = dict['package']['killmail']['solar_system_id']
        totalValue = dict['package']['zkb']['totalValue'] + 0.0

        # ATTACKERS
        attacker_amount = len(dict['package']['killmail']['attackers'])
        attacker_is_npc = dict['package']['zkb']['npc']
        attacker_is_solo = dict['package']['zkb']['solo']
        attacker_is_awox = dict['package']['zkb']['awox']
        attacker_ship_str = GetAttackerShips(dict)

        # VICTIM
        victim_damage_taken = dict['package']['killmail']['victim']['damage_taken']
        victim_shipID = dict['package']['killmail']['victim']['ship_type_id']
        logger.debug("victim_shipID: {}".format(victim_shipID))
        victim_ship_name = ''
        # resolve ship_name with invTypes.csv
        with open('invTypes.csv', newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                if row[0] == str(victim_shipID):
                    victim_ship_name = row[2]

        # GET NAMES FROM IDs
        victim_names = FetchVictimNameWithId(dict)
        attacker_names = FetchAttackerNameWithId(dict)

        # CHARACTER IDs
        attacker_char_name = ';'
        victim_char_name = ''

        for entry in attacker_names:
            if entry['category'] == 'character':
                attacker_char_name = attacker_char_name + entry['name'] + ';'

        for entry in victim_names:
            if entry['category'] == 'character':
                victim_char_name = entry['name']

        # CORPORATION IDs
        attacker_corp_name = ';'
        victim_corp_name = ''

        for entry in attacker_names:
            if entry['category'] == 'corporation':
                attacker_corp_name = attacker_corp_name + entry['name'] + ';'

        for entry in victim_names:
            if entry['category'] == 'corporation':
                victim_corp_name = entry['name']

        # ALLIANCE IDs
        attacker_alliance_name = ';'
        victim_alliance_name = ''

        for entry in attacker_names:
            if entry['category'] == 'alliance':
                attacker_alliance_name = attacker_alliance_name + entry['name'] + ';'

        for entry in victim_names:
            if entry['category'] == 'alliance':
                victim_alliance_name = entry['name']

        # LOGGER
        logger.info("killID: {}".format(killID))
        logger.info("killmail_time: {}".format(killmail_time))
        logger.debug("solar_systemID: {}".format(solar_systemID))
        logger.debug("totalValue: {}".format(totalValue))

        logger.debug("attackers_amount: {}".format(attacker_amount))
        logger.debug("attacker_is_npc: {}".format(attacker_is_npc))
        logger.debug("attacker_is_solo: {}".format(attacker_is_solo))
        logger.debug("attacker_is_awox: {}".format(attacker_is_awox))
        logger.debug("attacker_char_name: {}".format(attacker_char_name))
        logger.debug("attacker_corp_name: {}".format(attacker_corp_name))
        logger.debug("attacker_alli_name: {}".format(attacker_alliance_name))

        logger.debug("victim_damage_taken: {}".format(victim_damage_taken))
        logger.debug("victim_ship_name: {}".format(victim_ship_name))
        logger.debug("victim_char_name: {}".format(victim_char_name))
        logger.debug("victim_corp_name: {}".format(victim_corp_name))
        logger.debug("victim_alli_name: {}".format(victim_alliance_name))

        # ASSEMBLING NEW JSON BODY
        json_body = [{"measurement": "kills",
            "tags": {
                    "solar_systemID": solar_systemID,

                    "attacker_is_npc": attacker_is_npc,
                    "attacker_is_solo": attacker_is_solo,
                    "attacker_is_awox": attacker_is_awox,
                    "attacker_char_name": attacker_char_name,
                    "attacker_corp_name": attacker_corp_name,
                    "attacker_alliance_name": attacker_alliance_name,
                    "attacker_ship_str": attacker_ship_str,

                    "victim_char_name": victim_char_name,
                    "victim_corp_name": victim_corp_name,
                    "victim_alliance_name": victim_alliance_name,
                    "victim_ship_name": victim_ship_name
            },
            "fields": {
                    "#kills": 1,
                    "totalValue": totalValue,
                    "attacker_amount": attacker_amount,
                    "victim_damage_taken": victim_damage_taken,
            },
            "time": killmail_time,
            "time_prescision": "s"
        }]

        # WRITING TO DATABASE
        client.write_points(json_body, protocol='json')

        now = datetime.datetime.now()
        processing_time = now - then

        if len(last100_processing_time) > 100:
            last100_processing_time[1:]
        last100_processing_time.append(processing_time.total_seconds())
        avg_processing_time = sum(last100_processing_time) / len(last100_processing_time)

        logger.info("last100 avg processing time: {}".format(avg_processing_time))
        logger.info("processing time: {}".format(processing_time))
        logger.info("runtime: {}".format(now - start))
        logger.info("counter: {}\n".format(counter))

        counter = counter + 1
