import threading
import logging
import os
import csv

class NameFetcher2(threading.Thread):

    def __init__(self, unprocessed_killmail):
        threading.Thread.__init__(self)
        self.unprocessed_killmail = unprocessed_killmail
        self.logger = logging.getLogger(__name__ + ".NameFetcher2")

    def csv_inv_groups_scraper(self, group_id_list):
        group_name_list = []

        filepath = os.path.dirname(__file__) + "/ressources/invGroups.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                for l in range(0, len(group_id_list)):
                    if row[0] == str(group_id_list[l]):
                        group_name_list.append(row[2])
        self.logger.debug("Group Name List: {}".format(group_name_list))

        return {"group_name_list": group_name_list}

    def csv_inv_types_scraper(self, ship_id_list):
        name_list = []
        group_id_list = []

        filepath = os.path.dirname(__file__) + "/ressources/invTypes.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                for l in range(0, len(ship_id_list)):
                    if row[0] == str(ship_id_list[l]):
                        name_list.append(row[2])
                        group_id_list.append(row[1])

        self.logger.debug("Name List: {}".format(name_list))
        self.logger.debug("Group ID List: {}".format(group_id_list))

        return {"name_list": name_list, "group_id_list": group_id_list}

    def csv_map_solar_systems_scraper(self, solar_system_id_list):
        solar_system_name_list = []
        solar_system_security_list = []
        region_id_list = []
        constellation_id_list = []

        filepath = os.path.dirname(__file__) + "/ressources/mapSolarSystems.csv"
        with open(filepath, newline='') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                for l in range(0, len(solar_system_id_list)):
                    if row[2] == str(solar_system_id_list[l]):
                        solar_system_name_list.append(row[3])
                        region_id_list.append(row[0])
                        constellation_id_list.append(row[1])
                        solar_system_security_list.append(row[21])

        self.logger.debug("Solar System Name List: {}".format(solar_system_name_list))
        self.logger.debug("Solar System Security List: {}".format(solar_system_security_list))
        self.logger.debug("Region ID List: {}".format(region_id_list))
        self.logger.debug("Cosntellation ID List: {}".format(constellation_id_list))

        return {"solar_system_name_list": solar_system_name_list,
                "solar_system_security_list": solar_system_security_list,
                "region_id_list": region_id_list,
                "constellation_id_list": constellation_id_list}
