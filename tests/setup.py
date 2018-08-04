import unittest

from tests import killmail_tests
from tests import name_fetcher_tests
from tests import attacker_name_fetcher_tests
from tests import victim_name_fetcher_tests
from tests import solar_system_name_fetcher_tests
from tests import esi_call_tests
from tests import redisq_tests
from tests import influx_pusher_tests
from tests import main_tests
from tests import ship_name_fetcher_tests
from tests import victim_ship_name_fetcher_tests
from tests import attacker_ship_name_fetcher_tests


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
        uk12 = missing alliance
        uk13 = invalid alliance
        uk14 = missing ship
        uk15 = invalid ship

        V I C T I M :
        uk20 = missing char
        uk21 = invalid char
        uk22 = missing corp
        uk23 = invalid corp
        uk22 = missing alliance
        uk23 = invalid alliance
        uk24 = missing ship
        uk25 = invalid ship

        M U L T I P L E   A T T A C K E R S :
        uk8 =


        """

        self.uk1 = \
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
