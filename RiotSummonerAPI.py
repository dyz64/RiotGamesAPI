import RiotConstants as Constants
import requests

class RiotSummonerAPI(object):

#Constructor
    def __init__(self, api_key, region=Constants.REGIONS['NA']):
        self.api_key = api_key
        self.region = region

#Calling the API using requests package
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Constants.SUMMONER_URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args
            )

        print(response.url)
        return response.json()

#Summoner API methods
    def get_summoner_by_name(self, name):
        api_url=Constants.SUMMONER_URL['summoner_by_name'].format(
            version=Constants.API_VERSION['summoner'],
            names=name
        )
        # v{version}/summoner/by-name/{names}
        return self._request(api_url)


    def get_summoner_by_id(self, id):
        api_url=Constants.SUMMONER_URL['summoner_by_id'].format(
            version=Constants.API_VERSION['summoner'],
            id=id
        )
        return self._request(api_url)

    def get_masteries_by_summoner_id(self, id):
        api_url=Constants.SUMMONER_URL['masteries_by_summoner_id'].format(
            version=Constants.API_VERSION['summoner'],
            id=id
        )
        return self._request(api_url)

    def get_summoner_name_by_id(self, id):
        api_url=Constants.SUMMONER_URL['summoner_name_by_id'].format(
            version=Constants.API_VERSION['summoner'],
            id=id
        )
        return self._request(api_url)

    def get_runes_by_id(self, id):
        api_url=Constants.SUMMONER_URL['runes_by_id'].format(
            version=Constants.API_VERSION['summoner'],
            id=id
        )
        return self._request(api_url)
