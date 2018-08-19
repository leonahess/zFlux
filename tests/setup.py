import unittest

from killmail import Killmail
from name_fetcher import NameFetcher
from attacker_name_fetcher import AttackerNameFetcher
from attacker_ship_name_fetcher import AttackerShipNameFetcher
from victim_name_fetcher import VictimNameFetcher
from victim_ship_name_fetcher import VictimShipNameFetcher
from redisq import RedisQ
from esi_call import EsiCall
from solar_system_name_fetcher import SolarSystemNameFetcher
from ship_name_fetcher import ShipNameFetchter


class Setup(unittest.TestCase):
    """A Class to host all the Setup data to avoid a lot of copy pasting between modules"""

    def setUp(self):
        """!killmails dont have items!

        C O M P L E T E :
        uk00 = complete Killmail

        A T T A C K E R :
        uk10 = missing char
        uk11 = invalid char
        uk12 = missing corp
        uk13 = invalid corp
        uk14 = missing alliance
        uk15 = invalid alliance
        uk16 = missing ship
        uk17 = invalid ship
        uk18 = all missing names

        V I C T I M :
        uk20 = missing char
        uk21 = invalid char
        uk22 = missing corp
        uk23 = invalid corp
        uk24 = missing alliance
        uk25 = invalid alliance
        uk26 = missing ship
        uk27 = invalid ship
        uk28 = all missing names

        M U L T I P L E   A T T A C K E R S :
        uk30 = complete Killmail

        uk31 = 1 missing char
        uk32 = 2 missing char

        uk33 = 1 invalid char
        uk34 = 2 invalid char

        uk35 = 1 missing corp
        uk36 = 2 missing corp

        uk37 = 1 invalid corp
        uk38 = 2 invalid corp

        uk39 = 1 missing alliance
        uk40 = 2 missing alliance

        uk41 = 1 invalid alliance
        uk42 = 2 invalid alliance

        uk43 = 1 missing ship
        uk44 = 2 missing ship

        uk45 = 1 invalid ship
        uk46 = 2 invalid ship

        M I S C :
        uk60 = missing solar system id
        """

        self.uk00 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        # A T T A C K E R S
        self.uk10 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk11 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181235234402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk12 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk13 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429234234368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk14 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk15 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 13548398765430081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk16 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk17 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 64567867476505,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk18 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        # V I C T I M
        self.uk20 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk21 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114235234300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk22 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk23 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 91243252348531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk24 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk25 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99009876543345607362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk26 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk27 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 3287262342358
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        self.uk28 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

        # M U L T I P L E   A T T A C K E R S
        self.uk30 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk31 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk32 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk33 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224133452364382597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk34 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 22418251435597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 9173145634515917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk35 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk36 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk37 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 8183462345601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk38 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 8182345601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 985312472367437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk39 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk40 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk41 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 990053234582,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk42 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 990013455382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 9900513456382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk43 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk44 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk45 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 2992546490,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29990,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk46 = \
            {
                "package":
                    {
                        "killID": 71933840,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 99005382,
                                        "character_id": 224182597,
                                        "corporation_id": 818601383,
                                        "damage_done": 959,
                                        "final_blow": False,
                                        "security_status": 4.7,
                                        "ship_type_id": 234723459990,
                                        "weapon_type_id": 29990
                                    }, {
                                        "alliance_id": 99005382,
                                        "character_id": 91715917,
                                        "corporation_id": 98567437,
                                        "damage_done": 778,
                                        "final_blow": True,
                                        "security_status": 0.9,
                                        "ship_type_id": 29934563490,
                                        "weapon_type_id": 2969
                                    }],

                                "killmail_id": 71933840,
                                "killmail_time": "2018-08-18T11:39:49Z",
                                "solar_system_id": 30000142,
                                "victim":
                                    {
                                        "alliance_id": 99003581,
                                        "character_id": 2113228085,
                                        "corporation_id": 98446928,
                                        "damage_taken": 1737,
                                        "position":
                                            {
                                                "x": -107303397020.36,
                                                "y": -18744981247.376,
                                                "z": 436489013090.49},
                                        "ship_type_id": 33468
                                    },
                                "war_id": 609116
                            },
                        "zkb":
                            {
                                "locationID": 60003760,
                                "hash": "905e1f9b42f08effd05a804b32fafc541a6d8f46",
                                "fittedValue": 65084309.91,
                                "totalValue": 227289291.33,
                                "points": 1,
                                "npc": False,
                                "solo": False,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71933840/905e1f9b42f08effd05a804b32fafc541a6d8f46/"
                            }
                    }
            }

        self.uk60 = \
            {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }

    def generateKillmailObjects(self):

        self.k00 = Killmail(self.uk00)

        self.k10 = Killmail(self.uk10)
        self.k11 = Killmail(self.uk11)
        self.k12 = Killmail(self.uk12)
        self.k13 = Killmail(self.uk13)
        self.k14 = Killmail(self.uk14)
        self.k15 = Killmail(self.uk15)
        self.k16 = Killmail(self.uk16)
        self.k17 = Killmail(self.uk17)
        self.k18 = Killmail(self.uk18)

        self.k20 = Killmail(self.uk20)
        self.k21 = Killmail(self.uk21)
        self.k22 = Killmail(self.uk22)
        self.k23 = Killmail(self.uk23)
        self.k24 = Killmail(self.uk24)
        self.k25 = Killmail(self.uk25)
        self.k26 = Killmail(self.uk26)
        self.k27 = Killmail(self.uk27)
        self.k28 = Killmail(self.uk28)

        self.k30 = Killmail(self.uk30)
        self.k31 = Killmail(self.uk31)
        self.k32 = Killmail(self.uk32)
        self.k33 = Killmail(self.uk33)
        self.k34 = Killmail(self.uk34)
        self.k35 = Killmail(self.uk35)
        self.k36 = Killmail(self.uk36)
        self.k37 = Killmail(self.uk37)
        self.k38 = Killmail(self.uk38)
        self.k39 = Killmail(self.uk39)
        self.k40 = Killmail(self.uk40)
        self.k41 = Killmail(self.uk41)
        self.k42 = Killmail(self.uk42)
        self.k43 = Killmail(self.uk43)
        self.k44 = Killmail(self.uk44)
        self.k45 = Killmail(self.uk45)
        self.k46 = Killmail(self.uk46)
