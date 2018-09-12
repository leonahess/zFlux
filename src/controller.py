import logging

from src.performance_analysis import PerformanceAnalysis
from src.logger import Logger
from src.redisq import RedisQ
from src.killmail import Killmail
from src.killmail_influx_pusher import KillmailInfluxPusher
from src.performance_influx_pusher import PerformanceInfluxPusher


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
        perf = PerformanceAnalysis()
        logger.info("Initialized Performance Analysis")

        # Create InfluxPusher instance
        influx_killmail = KillmailInfluxPusher()
        influx_perf = PerformanceInfluxPusher()

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
