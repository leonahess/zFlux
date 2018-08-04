import requests
import logging


class RedisQ:
    """Actually gets the Killmail from zKillboard.com"""

    def __init__(self):
        self.logger = logging.getLogger(__name__ + ".RedisQ")

    def makeCall(self):
        """Since I always had Issues with especially the json decoder but also the request call randomly throwing
        exceptions I just catch 'em all and throw away any possible Killmail since I am not after 100% of killmails
        but a better reliability."""
        while True:
            try:
                r = requests.get('https://redisq.zkillboard.com/listen.php', timeout=20)
            except (KeyboardInterrupt, SystemExit):
                raise
            except requests.exceptions.Timeout as e:
                self.logger.error("RedisQ Timeout: {}".format(e))
                continue
            except:
                self.logger.error("Whoopsie")
                continue

            try:
                killmail = r.json()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                self.logger.error("Whoopsie 2")
                continue

            if killmail["package"] is None:
                continue

            if r.status_code is not 200:
                continue

            return killmail
