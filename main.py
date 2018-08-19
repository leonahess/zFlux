import datetime
import logging
import sys

from redisq import RedisQ
from killmail import Killmail
from influx_pusher import InfluxPusher


def main():
    # just some performance metrics
    start = datetime.datetime.now()
    last100_processing_time = []
    counter = 0

    # logger stuff
    logging.basicConfig(filename='zKill_scraper_{}.log'.format(start), level=logging.INFO,
                        format='%(asctime)s %(name)s:%(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    # create influx_pusher object
    influx = InfluxPusher()

    while True:
        unprocessed_killmail = RedisQ.makeCall(RedisQ())

        then = datetime.datetime.now()

        killmail = Killmail(unprocessed_killmail)

        influx.writeToDatabase(killmail)

        now = datetime.datetime.now()
        processing_time = now - then

        if len(last100_processing_time) > 100:
            last100_processing_time.pop(0)
        last100_processing_time.append(processing_time.total_seconds())
        avg_processing_time = sum(last100_processing_time) / len(last100_processing_time)

        counter = counter + 1

        sys.stdout.write("\r{} Killmails processed with an avg processesing time of {}s per Killmail of the last 100. "
                         "Last Killmail took {}".format(counter, round(avg_processing_time, 3), processing_time))
        sys.stdout.flush()

        logger.info("Counter: {}".format(counter))
        logger.info("Processing Time: {}".format(processing_time))
        logger.info("Avg Processing Time: {}".format(round(avg_processing_time,3)))


if __name__ == "__main__":
    main()
