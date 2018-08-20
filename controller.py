import logging

from performance_analysis import PerformanceAnalysis
from logger import Logger
from redisq import RedisQ
from killmail import Killmail
from influx_pusher import InfluxPusher


class Controller:
    """Controller Class which is responsible for handeling all the data streams"""

    @staticmethod
    def main():
        """Core Loop"""

        # Create Logger Instance
        log = Logger()
        logger = logging.getLogger(__name__ + ".Controller")
        logger.info("Initialized Logger")

        # Create PerformanceAnalysis instance
        perf = PerformanceAnalysis()
        logger.info("Initialized Performance Analysis")

        # Create InfluxPusher instance
        influx = InfluxPusher()

        # Create RedisQ instance
        redis = RedisQ()

        while True:
            unprocessed_killmail = RedisQ.makeCall(redis)

            perf.setCycleStart()

            killmail = Killmail(unprocessed_killmail)

            influx.writeToDatabase(killmail)

            perf.setCycleEnd()
            perf.calcCycleStats()

            
if __name__ == "__main__":
        Controller.main()
