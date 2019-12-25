import socket
import time
# 该模块是udp套接字服务器端的最简单实现方法

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024



def udp4Server():
    try:
        # 因为udp是无连接的套接字所有服务器端不需要开启监听
        udp4SerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp4SerSock.bind(ADDR)
        while True:
            print('等待消息...')
            data,addr = udp4SerSock.recvfrom(BUFSIZE)
            print(data.decode('utf8'))
            udp4SerSock.sendto(('[%s ]'%time.ctime()).encode('utf8')+data,addr)
            print('...连接来自:',addr)
    except EOFError:
        udp4SerSock.close()
    except KeyboardInterrupt:
        udp4SerSock.close()


if __name__ == "__main__":
    udp4Server()