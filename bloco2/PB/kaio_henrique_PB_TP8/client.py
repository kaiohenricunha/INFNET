# TP 8
# Client

import socket

HOST = '192.168.0.206'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Hello server!'.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))