import configparser


class PropertiesParser(object):

    def __init__(self, propertyFile):
        self.propertyFile = propertyFile
        self.parser = configparser.ConfigParser()
        self.parser.read(propertyFile)


#https://wiki.python.org/moin/ConfigParserExamples

    # def getProperties(self, section):
    #     dict1 = {}
    #     options = self.parser.options(section)
    #     for option in options:
    #         try:
    #             dict1[option] = self.parser.get(section, option)
    #             if dict1[option] == -1:
    #                 print("skip: %s" % option)
    #         except:
    #             print("exception on %s!" % option)
    #             dict1[option] = None
    #     return dict1

    def getProperties(self, group, key):
        value = ''
        try:
            value = self.parser.get(group, key)
        except:
            print("Unable to parse properties file for: (" + group + "," + key + ")")
            raise
        return value



def main():


    # parser = configparser.ConfigParser()
    # parser.read('C:/Users/David Zou/PycharmProjects/RiotGamesAPI_GitHub/Properties.ini')
    #
    # output=parser.sections()
    # print(str(output))


    parser = PropertiesParser('Properties.ini')
    # print(parser.getProperties('API_Key')['apikey'])
    print(parser.getProperties('API_Key', 'apiKey'))
if __name__ == "__main__":
    main()


