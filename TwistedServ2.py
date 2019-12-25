from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TwistedProtocol(protocol.Protocol):
    def connectionMade(self):
        print('...连接来自:',self.transport.getPeer().host)

    def dataReceived(self, data):
        self.transport.write(('[%s] '%ctime()).encode('utf8')+data)



factory = protocol.Factory()
factory.protocol = TwistedProtocol

reactor.listenTCP(PORT,factory)
print('等待客户端连接...')
reactor.run()