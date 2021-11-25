import time, os, socket, pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname() 
PORT = 9999
HP = (HOST, PORT)
buffer = 1024

def one():
    list = []

    print("\Files\n")
    d1 = response[1]
    for key, d1 in d1.items():
        print(key)
        for attribute,value in d1.items():
            print('{}: {}'.format(attribute,value))
        print("")

    time.sleep(8)
    os.system('clear') 
    list.append(key)
    return list

def two():
    list = []
    print("\n2- Processes | PID\n")
    title_pid = ['Name:', 'PID:', 'Executable:', 'CPU(s):', 'Memory(MB):', ]               
    i = 0

    while i <= len(response):
        pid_info = [response[i][0], response[i][1], response[i][2], response[i][3], response[i][4]]
        i = i + 1                  
        for x,y in zip(title_pid,pid_info):
            print ('{:30}{:<30}'.format(x,y))
        print("")

    time.sleep(8)
    os.system('clear') 
    list.append(title_pid)
    return list

def three():
    list = []

    print("\n3 - Scheduled Functions\n")
    d1 = response[1]
    d2 = response[0]

    print('get_file()')
    print(d1)
    print('get_process()')
    print(d2)

    time.sleep(8)
    os.system('clear') 
    list.append(d1)
    list.append(d2)
    return list

def four():
    # print("\n6- Up Hosts\n")
    # list = []
    # nmap_info = ['NMAP INFO']
    # i = 0

    # while i <= len(response):
    #     nmap_info1 = [response[i][0]]
    #     i = i + 1
    #     for x,y in zip(nmap_info, nmap_info1):
    #         print('{:30}{:<30}'.format(x,y))
    #     print("")

    # time.sleep(8)
    # os.system('clear') 
    # list.append(nmap_info)
    # return list

    list = []

    print("\n4 - Up Hosts\n")
    d2 = response[0]

    print(d2)

    time.sleep(8)
    os.system('clear') 
    list.append(d2)
    return list

def five():
    list = []
    print("\n5- Ports\n")
    port_info = ['PORT INFO']
    i = 0

    while i <= len(response):
        port_info1 = [response[i][0]]
        i = i + 1
        for x,y in zip(port_info, port_info1):
            print('{:30}{:<30}'.format(x,y))
        print("")

    time.sleep(8)
    os.system('clear')
    list.append(port_info)
    return list

def six():
    list = []
    print("\n6- Network\n")
    title_network = ['IPv4:', 'IPv6:', 'Mask:', 'MAC:']
    valor_network = [response[0], response[1], response[2], response[3]]

    for x,y in zip(title_network,valor_network):
        print ('{:30}{:30}'.format(x,y))

    time.sleep(8)
    os.system('clear') 
    list.append(title_network)
    return list


def menu():
    print('============================')
    print('OPTIONS')
    print('============================')
    print('|1| File Info')
    print('|2| Processes | PID')
    print('|3| Scheduled Functions')
    print('|4| Up Hosts')
    print('|5| Ports')
    print('|6| Network')
    print('============================') 

try: 
    client.connect(HP)
    option = " "
    client.send(option.encode('utf-8')) 
    options = ("1","2", "3", "4", "5", "6")
    
    count = 1
    while count == 1:   
        menu()
        option = input('Type in your option: ')
        if (option in options):
            client.send(option.encode('utf-8'))
            bytes_resp = client.recv(buffer)
            response = pickle.loads(bytes_resp)          
            if option == "1":
                one()           
            elif option == "2":
                two()       
            elif option == "3":
                three()                         
            elif option == "4":  
                four()                                    
            elif option == "5":
                five()                 
            elif option == "6":
                six()
            elif option == '7':
                count == 2
            else:
                print('Invalid option. Try again...')              
except Exception as erro:
    print(str(erro))

client.close()
input("Press any key to exit...")