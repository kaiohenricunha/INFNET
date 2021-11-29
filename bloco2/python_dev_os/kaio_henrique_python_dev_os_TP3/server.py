import psutil, time, os, socket, pickle, sched
from hurry.filesize import size

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname() 
PORT = 8881
HP = (HOST, PORT)
buffer = 1024

server.bind(HP)
server.listen()
print("Server:", HOST, "waiting on the port", PORT, "Just a minute...")
(client, addr) = server.accept()
print("Client connected:", addr)

# TP4

def get_file(option):    
    dir = os.listdir() 
    notfound = "File not found..."
    
    for file in dir: 
        if os.path.isfile(file):
           if file == option: 
                file_size = os.path.getsize(file)
                file_size = size(file_size)
                return file_size
    return notfound

while True:
    option = client.recv(buffer)   
    if option.decode('utf-8') == " ":
        print("Connected.")   
    elif option.decode('utf-8') != " ":
        bytes_resp = pickle.dumps(get_file(option.decode('utf-8')))
        client.send(bytes_resp)

client.close()
server.close()
input("Press any key to exit...") 