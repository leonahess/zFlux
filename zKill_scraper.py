import requests
import datetime
from influxdb import InfluxDBClient

def FetchNameWithId(attacker_id_str, kind):
    v = requests.get('https://esi.tech.ccp.is/latest/{0}s/names/?{0}_ids={1}&datasource=tranquility'.format(kind, attacker_id_str))
    if(r.status_code == 200):
     attacker_name = v.json()
    else:
        attacker_name = ''
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
        attacker_name_str = attacker_name_str + attacker_name_dict[t]['{}_name'.format(kind)] + ';'
    return attacker_name_str

start = datetime.datetime.now()

client = InfluxDBClient(host='localhost', port=8086, database='eve')

i = 1
while True:
    r = requests.get('https://redisq.zkillboard.com/listen.php')
    dict = r.json()

    then = datetime.datetime.now()

    if(r.text == '{"package":null}'):
        print(r.text)

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

        attacker_charID = UniquifyingIds(dict, 'character')
        print("attacker_charID: {}".format(attacker_charID))
        if attacker_charID:
            attacker_char_name_dict = FetchNameWithId(attacker_charID, 'character')
            attacker_char_name = DictToString(attacker_char_name_dict, 'character')
        print("attacker_char_name: {}".format(attacker_char_name))

        attacker_corpID = UniquifyingIds(dict, 'corporation')
        print("attacker_corpID: {}".format(attacker_corpID))
        if attacker_corpID:
            attacker_corp_name_dict = FetchNameWithId(attacker_corpID, 'corporation')
            attacker_corp_name = DictToString(attacker_corp_name_dict, 'corporation')
        print("attacker_corp_name: {}".format(attacker_corp_name))

        attacker_allianceID = UniquifyingIds(dict, 'alliance')
        print("attacker_allianceID: {}".format(attacker_allianceID))
        if attacker_allianceID:
            attacker_alliance_name_dict = FetchNameWithId(attacker_allianceID, 'alliance')
            attacker_alliance_name = DictToString(attacker_alliance_name_dict, 'alliance')
        print("attacker_alliance_name: {}".format(attacker_alliance_name))


        # victim
        if 'character_id' in dict['package']['killmail']['victim']:
            victim_charID = dict['package']['killmail']['victim']['character_id']
            v = requests.get('https://esi.tech.ccp.is/latest/characters/names/?character_ids={}&datasource=tranquility'.format(victim_charID))
            victim_char_name = v.json()[0]['character_name']
        else:
            victim_charID = 0
            victim_char_name = 0
        victim_corpID = dict['package']['killmail']['victim']['corporation_id']
        v = requests.get('https://esi.tech.ccp.is/latest/corporations/names/?corporation_ids={}&datasource=tranquility'.format(victim_corpID))
        victim_corp_name = v.json()[0]['corporation_name']
        if "alliance_id" in dict['package']['killmail']['victim']:
            victim_allianceID = dict['package']['killmail']['victim']['alliance_id']
            v = requests.get('https://esi.tech.ccp.is/latest/alliances/names/?alliance_ids={}&datasource=tranquility'.format(victim_allianceID))
            victim_alliance_name = v.json()[0]['alliance_name']
        else:
            victim_allianceID = 0
            victim_alliance_name = 0
        victim_damage_taken = dict['package']['killmail']['victim']['damage_taken']
        victim_ship = dict['package']['killmail']['victim']['ship_type_id']


        # Debugprints
        print("killID: {}".format(killID))
        print("time: {}".format(killmail_time))
        print("solar_systemID: {}".format(solar_systemID))
        print("totalValue: {}".format(totalValue))

        print("attackers_amount: {}".format(attacker_amount))
        print("attacker_is_npc: {}".format(attacker_is_npc))
        print("attacker_is_solo: {}".format(attacker_is_solo))
        print("attacker_is_awox: {}".format(attacker_is_awox))

        print("victim_charID: {}".format(victim_charID))
        print("victim_char_name: {}".format(victim_char_name))
        print("victim_corpID: {}".format(victim_corpID))
        print("victim_corp_name: {}".format(victim_corp_name))
        print("victim_allianceID: {}".format(victim_allianceID))
        print("victim_alliance_name: {}".format(victim_alliance_name))
        print("victim_damage_taken: {}".format(victim_damage_taken))
        print("ship: {}".format(victim_ship))

        now = datetime.datetime.now()

        print("Systemtime: {}".format(now))
        print("processing time: {}".format(now - then))
        print("runtime: {}".format(now - start))
        print("counter: {}\n\n".format(i))

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

                    "victim_charID": victim_charID,
                    "victim_char_name": victim_char_name,
                    "victim_corpID": victim_corpID,
                    "victim_corp_name": victim_corp_name,
                    "victim_allianceID": victim_allianceID,
                    "victim_alliance_name": victim_alliance_name,
                    "victim_ship": victim_ship
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
