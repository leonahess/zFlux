import unittest


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
        uk70 = wh with 2 attacker with no alli
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

        self.uk70 ={
            "package":
                    {
                        "killID": 72012818,
                        "killmail":
                        {
                            "attackers":
                                [{
                                    "character_id": 94830824,
                                    "corporation_id": 98539465,
                                    "damage_done": 1085,
                                    "final_blow": False,
                                    "security_status": 4.6,
                                    "ship_type_id": 22456,
                                    "weapon_type_id": 22456
                                },
                                {
                                    "character_id": 95074071,
                                    "corporation_id": 98389109,
                                    "damage_done": 1002,
                                    "final_blow": True,
                                    "security_status": 3.8,
                                    "ship_type_id": 33470,
                                    "weapon_type_id": 2205
                                }],
                            "killmail_id": 72012818,
                            "killmail_time": "2018-08-22T10:41:01Z",
                            "solar_system_id": 31000153,
                            "victim":
                                {
                                    "character_id": 2112516399,
                                    "corporation_id": 1000180,
                                    "damage_taken": 2087,
                                    "faction_id": 500001,
                                    "position":
                                        {
                                            "x": -640253952528.6340332031,
                                            "y": -106856446836.6681518555,
                                            "z": 706723188313.1087646484
                                        },
                                    "ship_type_id": 33468
                                }
                        },
                    "zkb":
                        {
                            "locationID": 40358750,
                            "hash": "bliblablup",
                            "fittedValue": 10593294.36,
                            "totalValue": 71262264.86,
                            "points": 2,
                            "npc": False,
                            "solo": False,
                            "awox": False,
                            "href": "https://esi.evetech.net/latest/killmails/72012818/a9c2729c80677483802d5be43a711441fd08670d/"
                        }
                    }
        }

        self.uk71 = {
            'package':
                {
                    'killID': 72477866,
                    'killmail':
                        {
                            'attackers':
                                [{
                                    'damage_done': 5548,
                                    'faction_id': 500021,
                                    'final_blow': True,
                                    'security_status': 0,
                                    'ship_type_id': 48930
                                }],
                            'killmail_id': 72477866,
                            'killmail_time': '2018-09-18T12:00:28Z',
                            'solar_system_id': 30002457,
                            'victim':
                                {
                                    'alliance_id': 99005338,
                                    'character_id': 93415043,
                                    'corporation_id': 98388312,
                                    'damage_taken': 5548,
                                    'position':
                                        {
                                            'x': -135325276843.07732,
                                            'y': -12429544064.941017,
                                            'z': -854682512095.4653
                                        },
                                    'ship_type_id': 589
                                }
                        },
                    'zkb':
                        {
                            'locationID': 40156317,
                            'hash': 'a80c7cacd7b04a69def30891a5fa76a19c2e72cb',
                            'fittedValue': 328402.77,
                            'totalValue': 614449.97,
                            'points': 1,
                            'npc': True,
                            'solo': False,
                            'awox': False,
                            'href': 'https://esi.evetech.net/v1/killmails/72477866/a80c7cacd7b04a69def30891a5fa76a19c2e72cb/'
                        }
                }
        }

        self.uk72 = \
            {
                'package':
                    {
                        'killID': 72478369,
                        'killmail':
                            {
                                'attackers':
                                    [{
                                        'damage_done': 3160,
                                        'faction_id': 500021,
                                        'final_blow': True,
                                        'security_status': 0,
                                        'ship_type_id': 48799
                                    }],
                                'killmail_id': 72478369,
                                'killmail_time': '2018-09-18T13:01:24Z',
                                'solar_system_id': 30001718,
                                'victim':
                                    {
                                        'alliance_id': 99007175,
                                        'character_id': 1388637030,
                                        'corporation_id': 98017240,
                                        'damage_taken': 3160,
                                        'position':
                                            {
                                                'x': -243396761509.71545,
                                                'y': -136410538661.06255,
                                                'z': 183045971513.31302}, 'ship_type_id': 34317
                                    }
                            },
                        'zkb':
                            {
                                'locationID': 40109337,
                                'hash': 'c5fb11ff0fa76495835965ec230efa037cecca55',
                                'fittedValue': 37301202.41,
                                'totalValue': 50309060.11,
                                'points': 1,
                                'npc': True,
                                'solo': False,
                                'awox': False,
                                'href': 'https://esi.evetech.net/v1/killmails/72478369/c5fb11ff0fa76495835965ec230efa037cecca55/'
                            }
                    }
            }
