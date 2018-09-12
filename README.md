# zFlux
Pulls every kill [zKill](https://zkillboard.com) gets and puts them into a 
[InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)
for making nice graphs.
 
Example Graphs made with [Grafana](https://grafana.com):
![example_graph1](src/ressources/zFlux1.PNG)
![example_graph2](src/ressources/zFlux2.PNG)
![example_graph3](src/ressources/zFlux3.PNG)
## Requirements

#### Python3

##### required modules:
```
influxdb
requests
```
Install with with ``pip3 install <package>``

If you don't have pip3 installed install it with ``sudo apt-get install python3-pip``

##### [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)
You will want a machine with Influx running. The script checks if there is a database called
'eve' and will otherwise create one. I recommend at least 4GB of RAM on your machine, though 
it might not enough if you plan to run the script longterm.
You also will want to disable the series limit in the config.


## Getting started

##### Edit the config.json

edit the config

run ``python3 zFlux.py``

## Available Data Points

### eve

##### measurement
``
kills
``

##### tags
```
kill_id

solar_system_id
solar_system_name
solar_system_security
solar_system_class
region_id
region_name
constellation_id
constellation_name


final_blow_ship_id
final_blow_ship_name
final_blow_ship_group_id
final_blow_ship_group_name

attacker_char_ids
attacker_char_names
attacker_corp_ids
attacker_corp_names
attacker_alliance_ids
attacker_alliance_names
attacker_is_npc
attacker_is_solo
attacker_is_awox
attacker_ship_ids
attacker_ship_names
attacker_ship_group_ids
attacker_ship_grouo_names

victim_char_id
victim_char_name
victim_corp_id
victim_corp_name
victim_alliance_id
victim_alliance_name
victim_ship_id
victim_ship_name
victim_ship_group_id
victim_ship_group_name
```
##### fields

```
#kills

value_total
value_fitted
value_ship

final_blow_damage
final_blow_damage_percent

victim_damage_taken
```

### performance

##### measurement
``
performance
``

##### tags
``
``
##### fields
````
#cycle
cycle_time
shortest_cycle
longest_cycle
avg100
avg1000
counter
````

## Class Diagram
![Class Diagramm](src/ressources/UML.png)

