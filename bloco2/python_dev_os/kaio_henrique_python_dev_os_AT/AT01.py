import psutil,os
from time import sleep

def info_processos_do_sistema():
    lista = []
    for proc in psutil.process_iter(): # iterates over all running processes
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name','memory_percent','cpu_percent']) # Process class' attribute names
        except psutil.NoSuchProcess:
            pass
        else:
            lista.append(pinfo)    
    return lista

if __name__ == "__main__": # module is being executed by itself
    while True:
        # os.system('clear')
        lista = info_processos_do_sistema()
        for i in lista: # iterates over all captured running processes and prints their info according to their attributes
            print("\Processo: " + i["name"] + " - PID: " + str(i["pid"]) + "\nUso de CPU: " + str(i["cpu_percent"]) + " %"+ "\nUso de Memória: " + str(i["memory_percent"]) + " %")       
        sleep(10)  