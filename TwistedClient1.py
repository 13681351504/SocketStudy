from twisted.internet import protocol,reactor


HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    # 自建方法
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %s...'%data)
            self.transport.write(data.encode('utf8'))
        else:
            self.transport.loseConnection()


    # 当socket连接时调用此方法
    def connectionMade(self):
        self.sendData()

    # 当接受到消息时调用此方法
    def dataReceived(self, data):
        print(data.decode('utf8'))
        self.sendData()



class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
    lambda self,connector, reason: reactor.stop()



def runClient():
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()


