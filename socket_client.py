import socket
# 基于TCP/IP协议的客户端代码(最简单形式)
#     tcp4Client()是ipv4的代码
#     tcp6Client()是ipv6协议的代码
HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024
# ' fe80::a8e0:4817:5697:52e6%11'

def tcp4Client():
    tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpClient.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        else:
            tcpClient.send(data.encode('utf8'))
            data = tcpClient.recv(BUFSIZE)
            if not data:
                break
            else:print(data.decode('utf8'))

    tcpClient.close()


def tcp6Client():
    tcpClient = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    tcpClient.connect(ADDR)
    while True:
        data = input('> ')
        if not data:
            break
        else:
            tcpClient.send(data.encode('utf8'))
            data = tcpClient.recv(BUFSIZE)
            if not data:
                break
            else:
                print(data.decode('utf8'))

    print('会话结束...')
    tcpClient.close()





if __name__ == "__main__":
    tcp4Client()