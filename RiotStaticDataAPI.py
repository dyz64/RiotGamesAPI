import RiotConstants as Constants
import requests

class RiotStaticDataAPI(object):

    def __init__(self, api_key, region=Constants.REGIONS['NA']):
        self.api_key = api_key
        self.region = region
        self.proxy = "GLOBAL"

#Calling the API using requests package
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Constants.STATIC_DATA_URL['base'].format(
                proxy=self.proxy,
                region=self.region,
                url=api_url
            ),
            params=args
            )

        #print(response.url)
        return response.json()

    def get_rune_by_id(self, id, runeData):
        api_url=Constants.STATIC_DATA_URL['runes_by_runeID'].format(
            version=Constants.API_VERSION['static_data'],
            runeID=id
        )
        return self._request(api_url, runeData)