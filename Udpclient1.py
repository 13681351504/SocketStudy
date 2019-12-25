import socket
# 该模块实现了最简单的udp客户端代码

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024



def udpClient():
    ADDR = (HOST, PORT)
    try:
        # 因为udp是无连接的套接字所以直接发送就行不需要事先与服务器建立连接
        udpCli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        while True:
            data = input('> ')
            if not data:
                break
            else:
                # 目的地址及端口在sendto方法中
                udpCli.sendto(data.encode('utf8'),ADDR)
                data, ADDR = udpCli.recvfrom(BUFSIZE)
                if not data:
                    break
                else:
                    print(data.decode('utf8'))
    except KeyboardInterrupt:
        udpCli.close()



if __name__ == "__main__":
    udpClient()