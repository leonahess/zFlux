import time
import requests
import logging


class EsiCall:
    """Handles all calls to the CCP API for ID to Name Resolution"""

    def __init__(self):
        self.logger = logging.getLogger(__name__ + ".EsiCall")

    def makeCall(self, ids):
        """ Makes the Call to the API and tries not to die upon any exception and thus return no names after a couple of retries.
            I just return nothing instead of trying to get a good answer, since my foremost priority is stability and
            anything else would probably entail some quite complex data processing, so I just return nothing if something
            goes wrong.
        """
        retry_time = 0
        v = {}

        for x in range(0, len(ids)):
            try:
                ids.remove("")
            except ValueError:
                pass

        while retry_time < 2:
            if ids is []:
                break

            try:
                v = requests.post('https://esi.evetech.net/latest/universe/names/?datasource=tranquility', json=ids)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                self.logger.error("Request Exception occcured")
                continue

            self.logger.debug("EsiCall Response_code: {}".format(v.status_code))

            if v.status_code == 200 or v.status_code == 404 or v.status_code == 400:
                break

            if v.status_code == 420 or v.status_code == 500:
                time.sleep(65)

            if v.status_code == 503:
                time.sleep(150)

            time.sleep(2 ^ retry_time + 3)
            retry_time = retry_time + 1

        if v.status_code == 200:
            names = v.json()
        else:
            names = []

        self.logger.debug("names: {}".format(names))

        return names
