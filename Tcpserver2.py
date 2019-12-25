from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

# 该模块儿使用TCPServer,StreamRequestHandler来简单实现TCP服务端接口

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024

class MyRequestHandler(SRH):
    def handle(self):
        # StreamRequestHandler模块中原始handler方法默认代码只有一行pass
        # 当接受到一个 客户端请求时，会调用handler方法去处理
        print('...连接来自:',self.client_address)
        self.wfile.write(('[%s] '%ctime()).encode('utf8')+self.rfile.readline())
        # StreamRequestHandler方法将输入和输出套接字看做类似文件的对象，readline()方法是查看客户发来的消息
        # write方法是向客户发送消息


def tcpSRH():
    tcpServ = TCP(ADDR,MyRequestHandler)
    print('等待客户端连接')
    tcpServ.serve_forever()




