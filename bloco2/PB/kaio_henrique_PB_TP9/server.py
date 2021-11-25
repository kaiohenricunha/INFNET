import psutil, time, os, socket, pickle, sched

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname() 
PORT = 9999
HP = (HOST, PORT)
buffer = 1024

server.bind(HP)
server.listen()
print("Server:", HOST, "waiting on the port", PORT, "Just a minute...")
(client, addr) = server.accept()
print("Client connected:", addr)

# TP4

def get_file():    
    start = time.time()
    dir = os.listdir() 
    dir_list = [] 
    dic_file_data = {}   
    d2 = {} 
    for file in dir: 
        if os.path.isfile(file): 
            size=(round(os.stat(file).st_size / 1024)) # file size
            path=os.path.abspath(file) # file path
            filec=time.ctime(os.path.getctime(file)) # creation time
            filem=time.ctime(os.path.getmtime(file)) # last modification time
            filea=time.ctime(os.path.getatime(file)) # last access time
            d2={'Size (bytes)':size,'Path':path,'Criação':filec,'Last modification':filem,'Last access':filea} 
            dic_file_data.update({file:d2}) 
        else: 
            dir_list.append(file) 
    list = [dir_list, dic_file_data]    
    
    end = time.time()
    print("Time spent:", round((end-start),2), "second(s).")  
    return list

def pid():   
    start = time.time()   
    dic = {}
    key = 0
    
    for proc in psutil.process_iter():
        if proc.name() == 'python3':   
            processID = proc.pid        
            try:            
                processName = proc.name()
                processExecutable = proc.exe()
                processCpuTime = round(proc.cpu_times().user,2)
                processMemory = round((proc.memory_info().rss / (1024*1024)),2)             
                
                list = []
                list.append(processName)
                list.append(processID)
                list.append(processExecutable) 
                list.append(processCpuTime)
                list.append(processMemory) 

                dic[key] = list
                key = key + 1            
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): 
               pass   
    end = time.time()
    print("Time spent:", round((end-start),2), "second(s).\n")    
    return dic

# TP5

def scheduler():
    start = time.time()
    scheduler = sched.scheduler(time.time, time.sleep)

    # enter: delay, priority, function name, arguments tuple
    scheduler.enter(2, 1, get_file, ())
    scheduler.run()
    end_file = time.time()

    scheduler.enter(3, 1, pid, ())
    scheduler.run()
    end_pid = time.time()

    duration_file = abs(end_file - start) # abs() returns an absolute value
    duration_pid = abs(end_pid - start)

    lista_info = []
    print("Finishing the scheduled functions...")
    info1 = (f" Time spent: {duration_file:.0f} seconds")
    info2 = (f" Time spent: {duration_pid:.0f} seconds")
    lista_info.append(info1)
    lista_info.append(info2)

    end = time.time()
    print("Total time spent:", round((end-start),2), "second(s).")  
    return lista_info

# TP6

def up_hosts():
    start = time.time()
    up_hosts = os.system(f"nmap -sP  {HOST}")

    end = time.time()
    print("Time spent:", round((end-start),2), "second(s).")  
    return up_hosts

def port_nmap():
    start = time.time()
    ports = os.system(f"nmap -p- {HOST}")

    end = time.time()
    print("Time spent:", round((end-start),2), "second(s).")  
    return ports

# TP7

def network():
    start = time.time()

    interfaces = psutil.net_if_addrs()
    names = []

    for i in interfaces:
        names.append(str(i))
        dic_itf = psutil.net_if_addrs()
        
        list = []
        ipv4 = dic_itf[names[0]][1][1]
        ipv6 = dic_itf[names[0]][2][1]
        mask = dic_itf[names[0]][1][2]
        mac = dic_itf[names[0]][0][1]

        list.append(ipv4)
        list.append(ipv6)
        list.append(mask)
        list.append(mac)       
        
    end = time.time()
    print("Time spent:", round((end-start),2), "seconds(s).")    
    return list

while True:
    option = client.recv(buffer)   
    if option.decode('utf-8') == " ":
        print("Connected.")   
    elif option.decode('utf-8') == "1":
        bytes_resp = pickle.dumps(get_file())
        client.send(bytes_resp)
    elif option.decode('utf-8') == "2":
        bytes_resp = pickle.dumps(pid())
        client.send(bytes_resp)      
    elif option.decode('utf-8') == "3":
        bytes_resp = pickle.dumps(scheduler())
        client.send(bytes_resp)   
    elif option.decode('utf-8') == "4":
        bytes_resp = pickle.dumps(up_hosts())
        client.send(bytes_resp)      
    elif option.decode('utf-8') == "5":
        bytes_resp = pickle.dumps(port_nmap())
        client.send(bytes_resp)      
    elif option.decode('utf-8') == "6":
        bytes_resp = pickle.dumps(network())
        client.send(bytes_resp)

client.close()
server.close()
input("Press any key to exit...")