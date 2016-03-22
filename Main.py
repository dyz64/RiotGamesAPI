from RiotSummonerAPI import RiotSummonerAPI
from RiotStaticDataAPI import RiotStaticDataAPI
def main():

    api=RiotSummonerAPI('ab158987-39f9-40a2-a3ae-5fcda9adebc7')
    staticDataAPI=RiotStaticDataAPI('ab158987-39f9-40a2-a3ae-5fcda9adebc7')


    summonerName='tehpandavan'

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

    runePage1=runes[str(id)]['pages'][1]
    print(runePage1)

    numRunePages=len(runes[str(id)]['pages'])
    print(type(numRunePages))
    print(numRunePages)

    for x in range(0, numRunePages):
        print("Rune Page #" + str(x+1) + " Name: " + runes[str(id)]['pages'][(x)]['name'])


    numRunesRunePage1=len(runePage1['slots'])
    listOfRuneNames={}
    for x in range(0, numRunesRunePage1):
        runeID=runePage1['slots'][x]['runeId']
        #print("Rune ID: " + str(runeID))
        runeStats=staticDataAPI.get_rune_by_id(str(runeID), {'runeData' : 'stats'})

        runeName = runeStats['name']
        if runeName not in listOfRuneNames.keys():
            # print(runeName)
            listOfRuneNames[runeName] = 1
        else:
            # print("ELSE " + runeName)
            runeCount = listOfRuneNames.pop(runeName)
            runeCount = runeCount + 1
            listOfRuneNames[runeName] = runeCount
        # print("Rune: " + runeStats['name'])


    for key, value in listOfRuneNames.items():
        print("Rune Name: " + key + " x" + str(value))




if __name__ == "__main__":
    main()