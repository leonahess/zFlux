# zKill_scraper
Pulls every kill zKill gets and puts them into a InfluxDB

## Requirements

#### Python3

##### required modules:
```
influxdb
requests
```
##### InfluxDB

## Set logging level

To not get too big logfiles you may set the logging level higher. Current Level is DEBUG
Other available logging levels:
  ```
  INFO
  WARNING
  ERROR
  ```
  ```
  logging.basicConfig(filename ='zKill_scraper_{}.log'.format(start), level = logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
  ```

## Available Data Points

#### Tags

###### General Information
```
killID
solar_systemID
```

###### Attacker Information
```
attacker_char_name
attacker_corp_name
attacker_alliance_name
attacker_is_npc
attacker_is_solo
attacker_is_awox
```

###### Victim Information
```
victim_char_name
victim_corp_name
victim_alliance_name
victim_ship_name
```
#### Fields

```
#kills
totalValue
victim_damage_taken
```
