import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig:


    @staticmethod
    def getbaseUrl():
        baseUrl = config.get('common info', 'baseUrl')
        return baseUrl

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password