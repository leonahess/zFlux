import logging
import datetime


class Logger:
    """Responsible for initializing the package wide logger"""

    def __init__(self):
        logging.basicConfig(filename='zKill_scraper_{}.log'.format(datetime.datetime.now()), level=logging.DEBUG,
                            format='%(asctime)s %(name)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)
