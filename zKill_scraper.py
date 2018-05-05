import requests
import datetime
import logging
import csv
from influxdb import InfluxDBClient

def FetchNameWithId(attacker_id_str, kind):
    while True:
        v = requests.get('https://esi.tech.ccp.is/latest/{0}s/names/?{0}_ids={1}&datasource=tranquility'.format(kind, attacker_id_str))
        if(v.status_code != 502):
            logger.warning("esi 502")
            break
    if(v.status_code == 200):
        try:
            attacker_name = v.json()
        except json.decoder.JSONDecodeError:
            logger.warning("esi json decode has failed!")
    else:
        attacker_name = []
    logger.debug("attacker_name: {}".format(attacker_name))
    return attacker_name

def UniquifyingIds(dict, kind):
    attacker_id = []
    attacker_id_str = ''
    for t in range(0, len(dict['package']['killmail']['attackers'])):
        if "{}_id".format(kind) in dict['package']['killmail']['attackers'][t] and dict['package']['killmail']['attackers'][t]['{}_id'.format(kind)] not in attacker_id:
            attacker_id.append(dict['package']['killmail']['attackers'][t]['{}_id'.format(kind)])
    for n in range(0, len(attacker_id)):
        attacker_id_str = attacker_id_str + str(attacker_id[n]) + ','
    attacker_id_str = attacker_id_str[:-1]
    return attacker_id_str

def DictToString(attacker_name_dict, kind):
    attacker_name_str = ';'
    for t in range(0, len(attacker_name_dict)):
        try:
            attacker_name_str = attacker_name_str + attacker_name_dict[t]['{}_name'.format(kind)] + ';'
        except KeyError:
            logger.warning("KeyError: {}".format(attacker_name))
    return attacker_name_str


start = datetime.datetime.now()

logging.basicConfig(filename ='zKill_scraper_{}.log'.format(start), level = logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

client = InfluxDBClient(host='localhost', port=8086, database='eve')

i = 1
while True:
    try:
        r = requests.get('https://redisq.zkillboard.com/listen.php?queueID=zKill_scaper', timeout = 20)
    except requests.exceptions.Timeout:
        logger.warning("zKill request timed out")
    try:
        dict = r.json()
    except json.decoder.JSONDecodeError:
        logger.warning("redisQ json decode has failed!")

    then = datetime.datetime.now()

    if(r.text == '{"package":null}'):
        logger.info(r.text)

    if(dict['package'] != None):
        # metadata
        killID = dict['package']['killID']
        killmail_time = dict['package']['killmail']['killmail_time']
        solar_systemID = dict['package']['killmail']['solar_system_id']
        totalValue = dict['package']['zkb']['totalValue'] + 0.0

        # attackers
        attacker_amount = len(dict['package']['killmail']['attackers'])
        attacker_is_npc = dict['package']['zkb']['npc']
        attacker_is_solo = dict['package']['zkb']['solo']
        attacker_is_awox = dict['package']['zkb']['awox']
        attacker_char_name = ''
        attacker_corp_name = ''
        attacker_alliance_name = ''


        # CHARACTER IDs
        attacker_charID = UniquifyingIds(dict, 'character')
        logger.debug("attacker_charID: {}".format(attacker_charID))
        victim_charID = []
        if 'character_id' in dict['package']['killmail']['victim']:
            victim_charID.append(dict['package']['killmail']['victim']['character_id'])
            logger.debug("victim_charID: {}".format(victim_charID))
            all_charID = attacker_charID + ',' + str(victim_charID[0])
        else:
            all_charID = attacker_charID
        logger.debug("all_charID: {}".format(all_charID))
        if all_charID:
            all_char_name_dict = FetchNameWithId(all_charID, 'character')
            logger.debug("all_char_name_dict: {}".format(all_char_name_dict))
            attacker_char_name_dict = all_char_name_dict
            victim_char_name = ''
            if victim_charID and all_char_name_dict:
                victim_char_name = all_char_name_dict[-1]['character_name']
                logger.info("victim_char_name: {}".format(victim_char_name))
                attacker_char_name_dict = all_char_name_dict[:-1]
            attacker_char_name = DictToString(attacker_char_name_dict, 'character')
            logger.info("attacker_char_name: {}".format(attacker_char_name))


        # CORPORATION IDs
        attacker_corpID = UniquifyingIds(dict, 'corporation')
        logger.debug("attacker_corpID: {}".format(attacker_corpID))
        victim_corpID = []
        if 'corporation_id' in dict['package']['killmail']['victim']:
            victim_corpID.append(dict['package']['killmail']['victim']['corporation_id'])
            logger.debug("victim_corpID: {}".format(victim_corpID))
            all_corpID = attacker_corpID + ',' + str(victim_corpID[0])
        else:
            all_corpID = attacker_corpID
        logger.debug("all_corpID: {}".format(all_corpID))
        if all_corpID:
            all_corp_name_dict = FetchNameWithId(all_corpID, 'corporation')
            logger.debug("all_corp_name_dict: {}".format(all_corp_name_dict))
            attacker_corp_name_dict = all_corp_name_dict
            victim_corp_name = ''
            if victim_corpID and all_corp_name_dict:
                victim_corp_name = all_corp_name_dict[-1]['corporation_name']
                logger.info("victim_corp_name: {}".format(victim_corp_name))
                attacker_corp_name_dict = all_corp_name_dict[:-1]
            attacker_corp_name = DictToString(attacker_corp_name_dict, 'corporation')
            logger.info("attacker_corp_name: {}".format(attacker_corp_name))


        # ALLIANCE IDs
        attacker_allianceID = UniquifyingIds(dict, 'alliance')
        logger.debug("attacker_allianceID: {}".format(attacker_allianceID))
        victim_allianceID = []
        if 'alliance_id' in dict['package']['killmail']['victim']:
            victim_allianceID.append(dict['package']['killmail']['victim']['alliance_id'])
            logger.debug("victim_allianceID: {}".format(victim_allianceID))
            all_allianceID = attacker_allianceID + ',' + str(victim_allianceID[0])
        else:
            all_allianceID = attacker_allianceID
        logger.debug("all_allianceID: {}".format(all_allianceID))
        if all_allianceID:
            all_alliance_name_dict = FetchNameWithId(all_allianceID, 'alliance')
            logger.debug("all_alliance_name_dict: {}".format(all_alliance_name_dict))
            attacker_alliance_name_dict = all_alliance_name_dict
            victim_alliance_name = ''
            if victim_allianceID and all_alliance_name_dict:
                victim_alliance_name = all_alliance_name_dict[-1]['alliance_name']
                logger.info("victim_alliance_name: {}".format(victim_alliance_name))
                attacker_alliance_name_dict = all_alliance_name_dict[:-1]
            attacker_alliance_name = DictToString(attacker_alliance_name_dict, 'alliance')
            logger.info("attacker_alliance_name: {}".format(attacker_alliance_name))


        victim_damage_taken = dict['package']['killmail']['victim']['damage_taken']
        logger.info("victim_damage_taken: {}".format(victim_damage_taken))
        victim_shipID = dict['package']['killmail']['victim']['ship_type_id']
        logger.debug("victim_shipID: {}".format(victim_shipID))
        victim_ship_name = ''
        # resolve ship_name with invTypes.csv
        with open('invTypes.csv', newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                if(row[0] == str(victim_shipID)):
                    victim_ship_name = row[2]
        logger.info("victim_ship_name: {}".format(victim_ship_name))



        # logger
        logger.info("killID: {}".format(killID))
        logger.info("time: {}".format(killmail_time))
        logger.info("solar_systemID: {}".format(solar_systemID))
        logger.info("totalValue: {}".format(totalValue))

        logger.info("attackers_amount: {}".format(attacker_amount))
        logger.info("attacker_is_npc: {}".format(attacker_is_npc))
        logger.info("attacker_is_solo: {}".format(attacker_is_solo))
        logger.info("attacker_is_awox: {}".format(attacker_is_awox))


        # assembling new json struct
        json_body = [{"measurement":"kills",
            "tags":{
                    "killID": killID,
                    "solar_systemID": solar_systemID,

                    "attacker_is_npc": attacker_is_npc,
                    "attacker_is_solo": attacker_is_solo,
                    "attacker_is_awox": attacker_is_awox,
                    "attacker_char_name": attacker_char_name,
                    "attacker_corp_name": attacker_corp_name,
                    "attacker_alliance_name": attacker_alliance_name,

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

        # writing to database
        client.write_points(json_body, protocol = 'json')
        i = i + 1

        now = datetime.datetime.now()

        logger.info("processing time: {}".format(now - then))
        logger.info("runtime: {}".format(now - start))
        logger.info("counter: {}\n".format(i))
