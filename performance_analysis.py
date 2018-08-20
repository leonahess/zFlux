import datetime
import time
import sys
import logging

class PerformanceAnalysis:
    """A class for measuring and storing vital performance metrics"""

    def __init__(self):
        """Initializing all the Variabl á la Java"""
        self.logger = logging.getLogger(__name__ + ".PerformanceAnalysis")

        self.start_time = datetime.datetime.now()
        self.cycle_start = datetime.datetime.now()
        self.cycle_end = datetime.datetime.now()
        self.cur_cycle = (self.cycle_end - self.cycle_start).total_seconds()

        time.sleep(1)

        self.shortest_cycle = (datetime.datetime.now() - self.start_time).total_seconds()
        self.longest_cycle = (datetime.datetime.now() - self.start_time).total_seconds()
        self.avg_last100_cycle = 0
        self.avg_last1000_cycle = 0
        self.counter = 0
        self.avg100_list = []
        self.avg1000_list = []

    def setCycleStart(self):
        """records the start of a cycle"""
        self.cycle_start = datetime.datetime.now()

    def setCycleEnd(self):
        """records the end of a cycle"""
        self.cycle_end = datetime.datetime.now()

    def calcCycleStats(self):
        """does all the work for the latest cycle"""
        self.cur_cycle = round((self.cycle_end - self.cycle_start).total_seconds(), 2)
        self.avg100()
        self.avg1000()

        if self.cur_cycle < self.shortest_cycle:
            self.shortest_cycle = round(self.cur_cycle, 2)

        if self.cur_cycle > self.longest_cycle:
            self.longest_cycle = round(self.cur_cycle, 2)

        self.counter += 1

        self.printStatus()
        self.logging()

    def avg100(self):
        """handles the averages of the last 100 cycles"""
        if len(self.avg100_list) > 100:
            self.avg100_list.pop(0)
        self.avg100_list.append(self.cur_cycle)
        self.avg_last100_cycle = round(sum(self.avg100_list) / len(self.avg100_list), 2)

    def avg1000(self):
        """handles the averages of the last 1000 cycles"""
        if len(self.avg1000_list) > 1000:
            self.avg1000_list.pop(0)
        self.avg1000_list.append(self.cur_cycle)
        self.avg_last1000_cycle = round(sum(self.avg1000_list) / len(self.avg1000_list), 2)

    def printStatus(self):
        """prints updating status line to the console"""
        sys.stdout.write("\r{} Killmails processed with an avg processesing time of {}s/{}s. "
                         "Latest: {}s at {}. Shortest: {}s Longest: {}s".format
                         (self.counter, self.avg_last100_cycle, self.avg_last1000_cycle, self.cur_cycle, datetime.datetime.now(),
                          self.shortest_cycle, self.longest_cycle))
        sys.stdout.flush()

    def logging(self):
        """logs all the metrics to the logfile"""
        self.logger.info("Current Cycle : {}s".format(self.cur_cycle))
        self.logger.info("Avg Last 100  : {}s".format(self.avg_last100_cycle))
        self.logger.info("Avg Last 1000 : {}s".format(self.avg_last1000_cycle))
        self.logger.info("Shortest Cycle: {}s".format(self.shortest_cycle))
        self.logger.info("Longest Cycle : {}s".format(self.longest_cycle))
