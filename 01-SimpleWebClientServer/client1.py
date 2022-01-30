import socket

clientsocket = 9000

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('127.0.0.1', clientsocket))
cmd = 'GET http://127.0.0.1/ HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
        data = mysocket.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

mysocket.close()