import time, os, socket, pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname() 
PORT = 8881
HP = (HOST, PORT)
buffer = 1024

def one():
    list = []

    print("\Files\n")
    
    print('Size: ', response)

try: 
    client.connect(HP)
    option = " "
    client.send(option.encode('utf-8')) 
    options = ("1", "7")
    
    count = 1
    while count == 1:   
        option = input('Type in your option: ')
        if (option in options):
            file = input('File name: ')
            client.send(file.encode('utf-8'))
            bytes_resp = client.recv(buffer)
            response = pickle.loads(bytes_resp)          
            if option == "1":
                one()
            elif option == '7':
                count == 2
            else:
                print('Invalid option. Try again...')              
except Exception as erro:
    print(str(erro))

client.close()
input("Press any key to exit...")