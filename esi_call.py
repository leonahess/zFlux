import time
import requests
import urllib3

class EsiCall:

    def makeCall(ids):
        retry_time = 0
        v = {}
        while retry_time < 2:
            try:
                v = requests.post('https://esi.tech.ccp.is/latest/universe/names/?&datasource=tranquility', json=ids)
            except requests.exceptions.ConnectionError as CErr:
                print(CErr)
            except urllib3.exceptions.MaxRetryError as MaxRetry:
                print(MaxRetry)
            except urllib3.exceptions.NewConnectionError as NewCErr:
                print(NewCErr)

            if v.status_code == 200:
                break

            time.sleep(2 ^ retry_time + 3)
            retry_time = retry_time + 1

        if v.status_code == 200:
            try:
                names = v.json()
            except ValueError as e:
                print(e)
        else:
            names = []

        return names
