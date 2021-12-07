import psutil,os
from time import sleep

def info_processos_do_sistema():
    lista = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name','memory_percent','cpu_percent']) # Process class' attribute names
        except psutil.NoSuchProcess:
            pass
        else:
            lista.append(pinfo)    
    return lista

if __name__ == "__main__":
    while True:
        os.system('cls||clear')
        lista = info_processos_do_sistema()
        for i in lista:
            print("\Processo: " + i["name"] + " - PID: " + str(i["pid"]) + "\nUso de CPU: " + str(i["cpu_percent"]) + " %"+ "\nUso de Memória: " + str(i["memory_percent"]) + " %")       
        sleep(10)  