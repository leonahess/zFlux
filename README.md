# zKill_scraper
Pulls every kill [zKill](zkillboard.com) gets and puts them into a 
[InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)
for making nice graphs.
 
Example Graph made with [Grafana](grafana.com):
![example_graph1](ressources/example_graph1.png)

For more example graphs take a look at [zKill_scraper_grafana_dashboard](https://github.com/leonhess/zKill_scraper_grafana_dashboard).

Usage:
```
python3 controller.py
```

## Requirements

#### Python3
Only tested on python 3.7.
##### required modules:
```
influxdb
requests
```
install with:
```
pip install influxdb
pip install requests
```
##### [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)
You will want a machine with Influx running. The script checks if there is a database called
'eve' and will otherwise create one. I recommend at least 4GB of RAM on your machine, though 
it might not enough if you plan to run the script longterm.
You also will want to disable the series limit in the config.


## Set logging level

To not get too big logfiles you may set the logging level higher in main.py. Current Level is INFO.
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

### eve

````
measurement = kills
````

##### tags
```
solar_system_name
solar_system_security
region_name
constellation_name
attacker_char_name
attacker_corp_name
attacker_alliance_name
attacker_is_npc
attacker_is_solo
attacker_is_awox
attacker_ship_name
victim_char_name
victim_corp_name
victim_alliance_name
victim_ship_name
```
##### fields

```
#kills
totalValue
victim_damage_taken
```

### performance

```` 
measurement = performance
````

##### tags
````

````
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
![Class Diagramm](ressources/UML.png)

