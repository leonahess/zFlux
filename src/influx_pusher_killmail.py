from src.influx_pusher import InfluxPusher


class InfluxPusherKillmail(InfluxPusher):

    def assembleJsonBody(self, killmail):
        """assembles a valid json construct for pushing the killmail to the database"""
        json_body = [{"measurement": "kills",
            "tags": {
                    "solar_system_name": killmail.solar_system_name,
                    "solar_system_security": killmail.solar_system_security,
                    "solar_system_class": killmail.system_class,
                    "region_name": killmail.region_name,
                    "constellation_name": killmail.constellation_name,
                    "attacker_is_npc": killmail.attacker_is_npc,
                    "attacker_is_solo": killmail.attacker_is_solo,
                    "attacker_is_awox": killmail.attacker_is_awox,

                    "attacker_char_name": killmail.attacker_char_name,
                    "attacker_corp_name": killmail.attacker_corp_name,
                    "attacker_alliance_name": killmail.attacker_alliance_name,
                    "attacker_ship_str": killmail.attacker_ship_names,

                    "victim_char_name": killmail.victim_char_name,
                    "victim_corp_name": killmail.victim_corp_name,
                    "victim_alliance_name": killmail.victim_alliance_name,
                    "victim_ship_name": killmail.victim_ship_name
            },
            "fields": {
                    "#kills": 1,
                    "totalValue": killmail.total_value,
                    "attacker_amount": killmail.attacker_amount,
                    "victim_damage_taken": killmail.victim_damage_taken,
            },
            "time": killmail.time,
            "time_precision": "s"
        }]

        return json_body

    def writeToDatabase(self, killmail):
        """pushes the json construct to the database"""
        json = self.assembleJsonBody(killmail)

        self.client.write_points(json, protocol="json")
