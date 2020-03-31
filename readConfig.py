import os
import codecs
import configparser

currentDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(currentDir, "config.ini")

class ReadConfig(object):
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        print(data)

    def get_WebURL(self, name):
        value = self.cf.get("WebURL", name)
        return value

    def get_HTTP(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_Email(self, name):
        value = self.cf.get("Email", name)
        return value

def main():
    rc = ReadConfig()

if __name__ == '__main__':
    main()