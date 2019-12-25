# TcpServer1.py
# 基于TCP/IP的服务端代码(最简单的形式)
#     tcp4Server()是ipv4协议代码
#     tcp6Server()是ipv6协议代码
import socket
import time

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024


# 基于tcp/ipv4 的server端
def tcp4Server():
    tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 创建套接字
    tcpSerSock.bind(ADDR) # 绑定地址端口
    tcpSerSock.listen(5) # 监听，参数代表同事接受的客户端请求数
    try:
        while True:
            print('等待客户端请求...')
            tcpcliSock,addr = tcpSerSock.accept()
            print('...请求来自:',addr)
            while True:
                data = tcpcliSock.recv(BUFSIZE)
                if not data:
                    print('会话结束...')
                    break
                else:
                    tcpcliSock.send(('[%s] '%time.ctime()).encode('utf8') + data)
            tcpcliSock.close()
            break
    except EOFError:
        tcpSerSock.close()
    except KeyboardInterrupt:
        tcpSerSock.close()
    finally:
        tcpSerSock.close()




# 基于tcp/ipv6 的server端
def tcp6Server():
    tcpServer = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    tcpServer.bind(ADDR)
    tcpServer.listen(6)
    try:
        while True:
            print('等待客户端连接...')
            seraccpt,addr = tcpServer.accept()
            print('...连接来自:',addr)
            while True:
                data = seraccpt.recv(BUFSIZE)
                if not data:
                    print('会话结束...')
                    break
                else:
                    seraccpt.send(('[%s]'%time.ctime()).encode('utf8')+data)
                    print(data.decode('utf8'))
            seraccpt.close() # 正常情况下服务端应该是不会关闭的
            break
    except EOFError:
        tcpServer.close()
    except KeyboardInterrupt:
        tcpServer.close()
    finally:
        tcpServer.close()



if __name__ == "__main__":
    tcp4Server()