# TP8
# Server

import socket, random

# HOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

print("Server addressed on", HOST, "is listening on port", PORT)

(communication_socket,addr) = server.accept()
print("Connected to:", str(addr))

while True:
    msg = communication_socket.recv(1024)
    if '$' == msg.decode('utf-8'):
        print('Closing connection with', addr)
        communication_socket.close()
        break
    elif '?' in msg.decode('utf-8'):
        resp = random.randint(0, 1)
        msg = "Yes\n"
        if resp == '0':
            msg = "No\n"
    else:
        msg = "Ok..." + msg.decode('utf-8')
    communication_socket.send(msg.encode('utf-8'))

server.close()
input("Press any key to exit...") 
    