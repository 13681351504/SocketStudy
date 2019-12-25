import socket


HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024

while True:
    sockClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockClient.connect(ADDR)
    data = input('> ')
    if not data:break
    else:
        sockClient.send(('%s\r\n'%data).encode('utf8'))
        data = sockClient.recv(BUFSIZE)
        if not data:break
        print(data.decode('utf8').strip())
        sockClient.close()