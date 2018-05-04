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
