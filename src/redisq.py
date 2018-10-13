import requests
import logging


class RedisQ:
    """Actually gets the Killmail from zKillboard.com"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def makeCall(self):
        """Since I always had Issues with especially the json decoder but also the request call randomly throwing
        exceptions I just catch 'em all and throw away any possible Killmail since I am not after 100% of killmails
        but a better reliability."""
        while True:
            try:
                self.logger.debug("Trying to get killmail from RedisQ")
                r = requests.get('https://redisq.zkillboard.com/listen.php', timeout=30)
            except (KeyboardInterrupt, SystemExit):
                raise
            except requests.exceptions.Timeout as e:
                self.logger.error("RedisQ Timeout: {}".format(e))
                continue
            except Exception as e:
                self.logger.error("RedisQ request failed: {}".format(e))
                continue

            try:
                killmail = r.json()
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                self.logger.error("RedisQ Json decode failed: {}".format(e))
                continue

            if killmail["package"] is None:
                self.logger.debug("No killmail was given")
                continue

            if r.status_code is not 200:
                self.logger.warning("RedisQ gave back a bad status: {}".format(r.status_code))
                continue

            self.logger.debug("RedisQ request was succesfull")
            return killmail
