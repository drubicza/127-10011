import time, os, sys, random
from time import sleep as timeout

def subscribe():
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Loading..'
    time.sleep(1)
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Sedang Membuka Youtube'
    time.sleep(1)
    os.system('xdg-open https://www.youtube.com/channel/UClb7JaAMtvIrBtRsFEbFZmg')
    time.sleep(1)
    os.system('clear')
    os.system('sh __client__.sh')


if __name__ == '__main__':
    subscribe()
