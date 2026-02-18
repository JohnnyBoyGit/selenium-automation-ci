import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_useremail():
        return config.get('common info', 'useremail')
