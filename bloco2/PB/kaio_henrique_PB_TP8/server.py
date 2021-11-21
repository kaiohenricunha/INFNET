# TP8
# Server

import socket, random

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

print("Server named", HOST, "is listening on port", PORT)

communication_socket, address = server.accept()

while True:
    msg = communication_socket.recv(1024)
    if '$' == msg.decode('utf-8'):
        print('Connection with', address, 'closed')
        communication_socket.close()
        break
    elif '?' in msg.decode('utf-8'):
        resp = str(random.randint(0, 1))
        msg = "Yes\n"
        if resp == '0':
            msg = "No\n"
        else:
            msg = "Ok..." + msg.decode('utf-8')
            communication_socket.send(msg.encode('utf-8'))

server.close()
input("Press any key to exit...") 
    