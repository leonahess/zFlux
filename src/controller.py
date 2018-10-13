import logging

from src.performance import Performance
from src.logger import Logger
from src.redisq import RedisQ
from src.killmail import Killmail
from src.influx_pusher_killmail import InfluxPusherKillmail
from src.influx_pusher_performance import InfluxPusherPerformance
from src.mongo_pusher import MongoPusher


class Controller:
    """Controller Class which is responsible for handeling all the data streams"""

    @staticmethod
    def main(config):
        """Core Loop"""

        # Create Logger Instance
        Logger(config['logging_level'])
        logger = logging.getLogger(__name__ + ".Controller")
        logger.disabled = config['disable_logging']
        logger.info("Initialized Logger")

        # Create PerformanceAnalysis instance
        perf = Performance()
        logger.info("Initialized Performance Analysis")

        # Create InfluxPusher instance
        if config['enable_influxdb'] is True:
            influx_killmail = InfluxPusherKillmail(config['influx']['ip'],
                                                   config['influx']['port'],
                                                   config['influx']['database_name'])

        influx_perf = InfluxPusherPerformance(config['influx']['ip'],
                                              config['influx']['port'],
                                              config['influx']['database_name'])

        # Create MongoPusher intance
        if config['enable_mongodb'] is True:
            mongo = MongoPusher(config['mongo']['ip'],
                                config['mongo']['port'],
                                config['mongo']['database_name'])

        # Create RedisQ instance
        redis = RedisQ()

        while True:
            unprocessed_killmail = RedisQ.makeCall(redis)

            perf.setCycleStart()

            if config['enable_mongodb'] is True:
                mongo.writeToDatabase(unprocessed_killmail)
                logger.debug("Wrote to Mongo")

            if config['enable_influxdb'] is True:
                killmail = Killmail(unprocessed_killmail)
                logger.debug("Processed Killmail")

                influx_killmail.writeToDatabase(killmail)
                logger.debug("wrote killmail to influx")

            perf.setCycleEnd()
            perf.calcCycleStats()

            if config['enable_performance_logging'] is True:
                influx_perf.writeToDatabase(perf)
                logger.debug("wrote performance to influx")
