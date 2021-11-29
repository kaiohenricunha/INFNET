import socket, pickle
from hurry.filesize import size

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = socket.gethostname()
PORT = 9991
HP = (HOST, PORT)
buffer = 1024

def disk_usage():
    d1 = response[0]
    d2 = response[1]
    d3 = response[2]

    print('============================')
    print('Disk Usage')
    print('============================')
    print('|1| Total Disk Space: {}'.format(size(d1)))
    print('|2| Used Disk Space: {}'.format(size(d2)))
    print('|3| Free Disk Space: {}'.format(size(d3)))
    print('============================\n\n\n')

def menu():
    print('============================')
    print('OPTIONS')
    print('============================')
    print('|1| Disk Usage')
    print('============================')

try:
    client.connect(HP)
    option = " "
    client.send(option.encode('utf-8'))
    options = ("1")

    count = 1
    while count == 1:
        menu()
        option = input('Type in your option: ')
        if (option in options):
            client.send(option.encode('utf-8'))
            bytes_resp = client.recv(buffer)
            response = pickle.loads(bytes_resp)
            if option == "1":
                disk_usage()
            else:
                print('Invalid option. Try again...')
except Exception as erro:
    print(str(erro))

client.close()
input("Press any key to exit...")