form socket import *

def createServer():
    serversocket = socket(AR_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while