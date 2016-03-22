from RiotSummonerAPI import RiotSummonerAPI

def main():
    api=RiotSummonerAPI('ab158987-39f9-40a2-a3ae-5fcda9adebc7')

    summonerName='voidseeker'

    resultByName = api.get_summoner_by_name(summonerName)

    print(type(resultByName))
    print("resultByName: " + str(resultByName))

    id=resultByName[summonerName.replace(" ","")]['id']
    #print('ID: ' + str(id))

    #resultByID = api.get_summoner_by_id(id)
    #print('resultByID: ' + str(resultByID))

    masteries = api.get_masteries_by_summoner_id(id)
    print("Masteries: " + str(masteries))


    runes = api.get_runes_by_id(id)
    print(type(runes))
    print("Rune: " + str(runes))

    runePages=runes[str(id)]['pages'][1]
    print(runePages)

    numRunePages=len(runes[str(id)]['pages'])
    print(type(numRunePages))
    print(numRunePages)

    for x in range(0, numRunePages):
        print("Rune Page #" + str(x+1) + " Name: " + runes[str(id)]['pages'][(x)]['name'])

    print("THIS IS A TEST COMMIT MESSAGE21245124")

if __name__ == "__main__":
    main()