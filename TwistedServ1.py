from time import ctime
from twisted.internet import protocol,reactor

# 定义端口号
PORT = 21567

# protocol.Protocol 和 protocol.Factory都是用来处理一些配置和协议的底层相关业务的，
# 不同之处在于protocol.Protocol是用来设置单个socket请求的特定配置
# protocol.Factory是用来设置持久的、多个socket可共享的通用配置

# 定义的类是处理单个socket的
class TSServProtocol(protocol.Protocol):
    # 当有客户请求接入的时候自动调用connectionMade方法
    def connectionMade(self):
        # 提取请求客户的ip
        clit = self.clit = self.transport.getPeer().host
        print('...连接来自:',clit)

    # 当有消息发送过来的时候自动调用dataReceived方法
    def dataReceived(self, data):
        self.transport.write(('[%s] '%ctime()).encode('utf8')+data)




def runserver():
    # 实例化协议工厂函数
    factory = protocol.Factory()
    # 设置持久的多个socket的通用配置
    factory.protocol = TSServProtocol
    print('等待客户连接')
    # 开始监听及设置回调函数
    reactor.listenTCP(PORT,factory)
    reactor.run()




