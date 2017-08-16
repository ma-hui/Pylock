from ConfigParser import  ConfigParser
import logging

def testConfig():
    '''
    config read from config.txt

    '''
    CONFIGFILE = 'config.txt'
    config = ConfigParser()
    config.read(CONFIGFILE)

    print config.get('messages','hello')
    print config.getint('numbers','lenth')

def Log(inf):
    logging.info(inf)

def testLog():
    logging.basicConfig(level=logging.INFO, filename='pylog.txt')
    Log('Start Logging')

if __name__ == '__main__':
    testConfig()
    testLog()


