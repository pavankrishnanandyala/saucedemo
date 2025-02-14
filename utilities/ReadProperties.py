import configparser

class ReadConfig:
    config = configparser.ConfigParser()
    config.read('..\\Configurations\\config.ini')

    @staticmethod
    def getbaseUrl():
        return ReadConfig.config.get('common info', 'baseUrl')

    @staticmethod
    def getusername():
        return ReadConfig.config.get('common info', 'username')

    @staticmethod
    def getpassword():
        return ReadConfig.config.get('common info', 'password')