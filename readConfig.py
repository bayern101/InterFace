import os
import codecs
import configparser

currentDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(currentDir, "config.ini")

class ReadConfig(object):
    def __init__(self):
        fd = open(configPath)
        data =fd.read()

    def getEmail(self, name):
        value = self.cf

def main():
    rc = ReadConfig()

if __name__ == '__main__':
    main()