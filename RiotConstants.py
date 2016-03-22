SUMMONER_URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}' ,
    'summoner_by_name': 'v{version}/summoner/by-name/{names}' ,
    'summoner_by_id':  'v{version}/summoner/{id}' ,
    'masteries_by_summoner_id': 'v{version}/summoner/{id}/masteries' ,
    'summoner_name_by_id': 'v{version}/summoner/{id}/name' ,
    'runes_by_id': 'v{version}/summoner/{id}/runes'

}

#https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/WiseGrandSky?api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
#https://na.api.pvp.net/api/lol/na/v1.4/summoner/20624939?api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
#https://na.api.pvp.net/api/lol/na/v1.4/summoner/20624939/masteries?api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
#https://na.api.pvp.net/api/lol/na/v1.4/summoner/20624939/name?api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
#https://na.api.pvp.net/api/lol/na/v1.4/summoner/20624939/runes?api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7



STATIC_DATA_URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/static-data/{region}/{url}' ,
    'runes_by_runeID': 'v{version}/rune/{runeID}'
}

#https://global.api.pvp.net/api/lol/static-data/na/v1.2/rune/5273?runeData=stats&api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
#https://GLOBAL.api.pvp.net/api/lol/static-data/NA/v1.2/rune/5345?runeData=stats&api_key=ab158987-39f9-40a2-a3ae-5fcda9adebc7
API_VERSION = {

    'summoner': '1.4',
    'static_data': '1.2'

}

REGIONS = {
    'NA':'na' ,
    'GLOBAL':'global'
}
