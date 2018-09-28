import logging
import datetime


class Logger:
    """Responsible for initializing the package wide logger"""

    def __init__(self, level):

        logging.basicConfig(filename='logs/zKill_scraper_{}.log'.format(datetime.datetime.now()),
                            level=self.return_level(level),
                            format='%(asctime)s %(name)s:%(levelname)s:%(message)s')

    @staticmethod
    def return_level(level):

        if level == "DEBUG":
            return logging.DEBUG
        elif level == "INFO":
            return logging.INFO
        elif level == "WARNING":
            return logging.WARNING
        elif level == "ERROR":
            return logging.ERROR
        elif level == "CRITICAL":
            return logging.CRITICAL
