from twisted.internet import protocol,reactor

HOST = 'localhost'
PORT = 21567

class ProtocolClient(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            self.transport.write(data.encode('utf8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()


    def dataReceived(self, data):
        print(data.decode('utf8'))
        self.sendData()



class ClientFactory(protocol.ClientFactory):
    protocol = ProtocolClient
    clientConnectionLost = clientConnectionFailed = \
    lambda self,connector,reason : reactor.stop()



reactor.connectTCP(HOST,PORT,ClientFactory())
reactor.run()