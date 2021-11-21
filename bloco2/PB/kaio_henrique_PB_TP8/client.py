# TP 8
# Client

import socket, sys

HOST = '127.0.0.1'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((HOST, PORT))
except Exception as error:
    print('Error:', error)
    sys.exit()

print("To exit, type '$'")
msg = input()
socket.send(msg.encode('utf-8'))
while msg != '$':
    msg = socket.recv(1024)
    print(msg.decode('utf-8'))
    msg = input()
    socket.send(msg.encode('utf-8'))

socket.close()