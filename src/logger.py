import logging
import datetime


class Logger:
    """Responsible for initializing the package wide logger"""

    def __init__(self, logging_level):
        logging.basicConfig(filename='logs/zKill_scraper_{}.log'.format(datetime.datetime.now()),
                            format='%(asctime)s %(name)s:%(levelname)s:%(message)s')
        level = logging.getLevelName(logging_level)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
