import logging

from src.performance import Performance
from src.logger import Logger
from src.redisq import RedisQ
from old.killmail import Killmail
from src.influx_pusher_killmail import InfluxPusherKillmail
from src.influx_pusher_performance import InfluxPusherPerformance


class Controller:
    """Controller Class which is responsible for handeling all the data streams"""

    @staticmethod
    def main(config):
        """Core Loop"""

        # Create Logger Instance
        log = Logger()
        logger = logging.getLogger(__name__ + ".Controller")
        logger.info("Initialized Logger")

        # Create PerformanceAnalysis instance
        perf = Performance()
        logger.info("Initialized Performance Analysis")

        # Create InfluxPusher instance
        influx_killmail = InfluxPusherKillmail()
        influx_perf = InfluxPusherPerformance

        # Create RedisQ instance
        redis = RedisQ()

        while True:
            unprocessed_killmail = RedisQ.makeCall(redis)

            perf.setCycleStart()

            killmail = Killmail(unprocessed_killmail)

            influx_killmail.writeToDatabase(killmail)

            perf.setCycleEnd()
            perf.calcCycleStats()

            influx_perf.writeToDatabase(perf)
