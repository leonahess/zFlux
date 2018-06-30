import requests
import datetime
import logging
import csv
from influxdb import InfluxDBClient


def EsiCall(ids):

    while True:
        v = requests.post('https://esi.tech.ccp.is/latest/universe/names/?&datasource=tranquility', json=ids)
        if v.status_code != 502:
            break
        logger.warning("esi 502")

    if v.status_code == 200:
        try:
            names = v.json()
        except ValueError as e:
            logger.warning("esi json decode has failed!: {}".format(e))
    else:
        names = []

    logger.debug("attacker_name: {}".format(names))

    return names


'''
def UniquifyingIds(dict, kind):
    attacker_id = []
    for t in range(0, len(dict['package']['killmail']['attackers'])):
        if "{}_id".format(kind) in dict['package']['killmail']['attackers'][t] and dict['package']['killmail']['attackers'][t]['{}_id'.format(kind)] not in attacker_id:
            attacker_id.append(dict['package']['killmail']['attackers'][t]['{}_id'.format(kind)])
    return attacker_id

def DictToString(attacker_name_dict, kind):
    attacker_name_str = ';'
    for t in range(0, len(attacker_name_dict)):
        try:
            attacker_name_str = attacker_name_str + attacker_name_dict[t]['{}_name'.format(kind)] + ';'
        except KeyError:
            logger.warning("KeyError: {}".format(attacker_name_str))
    return attacker_name_str
'''


def FetchVictimNameWithId(killmail):

    if 'character_id' in killmail['package']['killmail']['victim']:
        char_id = killmail['package']['killmail']['victim']['character_id']
    else:
        char_id = ''

    if 'corporation_id' in killmail['package']['killmail']['victim']:
        corp_id = killmail['package']['killmail']['victim']['corporation_id']
    else:
        corp_id = ''

    if 'alliance_id' in killmail['package']['killmail']['victim']:
        alliance_id = killmail['package']['killmail']['victim']['alliance_id']
    else:
        alliance_id = ''

    victim_ids = []

    if char_id != '':
        victim_ids.append(char_id)
    if corp_id != '':
        victim_ids.append(corp_id)
    if alliance_id != '':
        victim_ids.append(alliance_id)

    names = EsiCall(victim_ids)

    logger.debug("Victim char_id: {}".format(char_id))
    logger.debug("Victim corp_id: {}".format(corp_id))
    logger.debug("Victim alli_id: {}".format(alliance_id))
    logger.debug("Victim ids: {}".format(victim_ids))
    logger.debug("Victim names: {}".format(names))

    return names
'''
def GetName(dict, kind):
    attacker_ID = UniquifyingIds(dict, '{}'.format(kind))
    victim_ID = []
    logger.debug("attacker_{}ID: {}".format(kind, attacker_ID))

    if '{}_id'.format(kind) in dict['package']['killmail']['victim']:
        victim_ID.append(dict['package']['killmail']['victim']['{}_id'.format(kind)])
        logger.debug("victim_{}ID: {}".format(kind, victim_ID))
        all_ID =
    else:
        all_ID = attacker_ID
    logger.debug("all_{}ID: {}".format(kind, all_ID))

    if all_ID:
        all_name_dict = FetchNameWithId(all_ID, '{}'.format(kind))
        logger.debug("all_{}_name_dict: {}".format(kind, all_name_dict))
        attacker_name_dict = all_name_dict
        victim_name = ''

        if victim_ID and all_name_dict:
            victim_name = all_name_dict[-1]['{}_name'.format(kind)]
            logger.debug("victim_{}_name: {}".format(kind, victim_name))
            attacker_name_dict = all_name_dict[:-1]

        attacker_name = DictToString(attacker_name_dict, '{}'.format(kind))
        logger.debug("attacker_{}_name: {}".format(kind, attacker_name))
        final_name_dict = {"victim_name": victim_name, "attacker_name": attacker_name}
    else:
        final_name_dict = {"victim_name": '', "attacker_name": ''}

    logger.debug("final_name_dict: {}".format(final_name_dict))
    return final_name_dict
'''


def GetAttackerShips(dict):
    attacker_ship_list = []
    attacker_ship_name_list = []
    attacker_ship_name_str = ''

    for x in range(0, len(dict['package']['killmail']['attackers'])):
        try:
            if(dict['package']['killmail']['attackers'][x]['ship_type_id'] not in attacker_ship_list):
                attacker_ship_list.append(dict['package']['killmail']['attackers'][x]['ship_type_id'])
        except KeyError:
            logger.error("attacker ship key error")
    logger.debug("attacker_ship_list: {}".format(attacker_ship_list))

    with open('invTypes.csv', newline='') as f:
        inv_types = csv.reader(f)
        for row in inv_types:
            for l in range(0, len(attacker_ship_list)):
                if(row[0] == str(attacker_ship_list[l])):
                    attacker_ship_name_list.append(row[2])
    logger.debug("Ship name list: {}".format(attacker_ship_name_list))

    for k in range(0, len(attacker_ship_name_list)):
        attacker_ship_name_str = attacker_ship_name_str + ';' + attacker_ship_name_list[k]
    attacker_ship_name_str = attacker_ship_name_str + ';'
    logger.info("attacker_ships: {}".format(attacker_ship_name_str))

    return attacker_ship_name_str


start = datetime.datetime.now()

logging.basicConfig(filename ='zKill_scraper_{}.log'.format(start), level = logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

# Connect to Database and check if database 'eve' exists, otherwise create one
client = InfluxDBClient(host='localhost', port=8086, database='eve')
database_list = client.get_list_database()
eve_exists = False
for s in range(0, len(database_list)):
    if database_list[s]['name'] == 'eve':
        eve_exists = True
if eve_exists == False:
    client.create_database('eve')

last100_processing_time = []
counter = 1
while True:
    try:
        r = requests.get('https://redisq.zkillboard.com/listen.php?queueID=zKill_scaperDev', timeout = 20)
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

    if dict['package'] != None:

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

        # GET VICTIM NAMES
        victim_names = FetchVictimNameWithId(dict)

        # CHARACTER IDs
        attacker_char_name = ''
        victim_char_name = ''

        for entry in victim_names:
            if entry['category'] == 'character':
                victim_char_name = entry['name']

        # CORPORATION IDs
        attacker_corp_name = ''
        victim_corp_name = ''

        for entry in victim_names:
            if entry['category'] == 'corporation':
                victim_corp_name = entry['name']

        # ALLIANCE IDs
        attacker_alliance_name = ''
        victim_alliance_name = ''

        for entry in victim_names:
            if entry['category'] == 'alliance':
                victim_alliance_name = entry['name']



        # logger
        logger.info("killID: {}".format(killID))
        logger.info("killmail_time: {}".format(killmail_time))
        logger.info("solar_systemID: {}".format(solar_systemID))
        logger.info("totalValue: {}".format(totalValue))

        logger.info("attackers_amount: {}".format(attacker_amount))
        logger.info("attacker_is_npc: {}".format(attacker_is_npc))
        logger.info("attacker_is_solo: {}".format(attacker_is_solo))
        logger.info("attacker_is_awox: {}".format(attacker_is_awox))
        logger.info("attacker_char_name: {}".format(attacker_char_name))
        logger.info("attacker_corp_name: {}".format(attacker_corp_name))
        logger.info("attacker_alli_name: {}".format(attacker_alliance_name))

        logger.info("victim_damage_taken: {}".format(victim_damage_taken))
        logger.info("victim_ship_name: {}".format(victim_ship_name))
        logger.info("victim_char_name: {}".format(victim_char_name))
        logger.info("victim_corp_name: {}".format(victim_corp_name))
        logger.info("victim_alli_name: {}".format(victim_alliance_name))

        # ASSEMBLING NEW JSON BODY
        json_body = [{"measurement":"kills",
            "tags":{
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
            "fields":{
                    "#kills":1,
                    "totalValue": totalValue,
                    "attacker_amount": attacker_amount,
                    "victim_damage_taken": victim_damage_taken,
                },
            "time": killmail_time,
            "time_prescision":"s"
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
