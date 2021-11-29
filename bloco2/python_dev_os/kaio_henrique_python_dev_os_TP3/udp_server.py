import psutil,socket, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = socket.gethostname() 
PORT = 9991
HP = (HOST, PORT)
buffer = 1024

server.bind(HP)
print("Server:", HOST, "waiting on the port", PORT, "Just a minute...")

def disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage

while True:
    # option = client.recv(buffer)
    option, address = server.recvfrom(1024)
    if option.decode('utf-8') == " ":
        print("Connected.")   
    elif option.decode('utf-8') == "1":
        bytes_resp = pickle.dumps(disk_usage())
        server.sendto(bytes_resp, address)