import psutil
import os
import sys
import sched
import time
import ipaddress

def list_dir_files(path):
    """
    Função que lista os arquivos/diretórios de um diretório
    :param path:
    :return:
    """
    list_files = []
    for file in os.listdir(path):
        list_files.append(file)
    return list_files

def list_permissions(path):
    """
    Função que lista as permissões de um arquivo
    :param path:
    :return:
    """
    print([(4,"r - Read"),(2,"w - Write"),(1,"x - Execute")])
    mask = oct(os.stat(path).st_mode)[-3:]
    return mask

def list_processes():
    """
    Função que lista todos os processos
    :return:
    """
    # Lista os processos
    for proc in psutil.process_iter():
        try:
            print(proc.name(), proc.exe(), proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def list_processes_by_name(name):
    """
    Função que lista os processos por nome
    :param name:
    :return:
    """
    # Lista os processos
    for proc in psutil.process_iter():
        try:
            if proc.name() == name:
                print(proc.name(), proc.exe(), proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def list_resources_by_process(pid):
    """
    Função que lista os recursos de um processo
    :param pid:
    :return:
    """
    # Lista consumo de memória e cpu
    print("Memória: ", round((psutil.Process(pid).memory_info().rss))/(1024*1024), "MB")
    print("CPU: ", psutil.Process(pid).cpu_percent(), "%")
    print(psutil.Process(pid).cpu_times())


def list_all_network_interfaces():
    """
    Função que lista todas as interfaces de rede
    :return:
    """
    for interface in psutil.net_if_addrs():
        print(interface)

def list_network_info(interface):
    """
    Função que lista as informações de rede
    :return:
    """
    # Lista as informações de rede
    print("IPv4: ", psutil.net_if_addrs()[interface][0][1])
    print("IPv6: ", psutil.net_if_addrs()[interface][1][1])
    print("MAC: ", psutil.net_if_addrs()[interface][0][2])

def list_port_by_ip_using_nmap(ip):
    """
    Função que lista as portas disponíveis
    :param ip:
    :return:
    """
    # Lista as portas disponíveis
    print(os.system(f"nmap -p- {ip}"))

def scan_devices_in_network(subnet):
    """
    Função que lista os dispositivos na rede
    :return:
    """
    #192.168.1.0/24
    print(os.system(f"nmap -sP  {subnet}"))

def get_subnet_from_ip(ip):
    """
    Função que retorna o subnet de um IP
    :param ip:
    :return:
    """
    net = ipaddress.ip_interface(ip)
    print("Address", net.ip)
    print("Mask", net.netmask)
    print("Cidr", str(net.network).split('/')[1])
    print("Network", str(net.network).split('/')[0])
    print("Broadcast", net.network.broadcast_address)

def get_interface_consumption(interface):
    """
    Função que retorna o consumo de uma interface de rede
    :param interface:
    :return:
    """
    # Lista as informações de rede
    print("IPv4: ", psutil.net_if_addrs()[interface][0][1])
    print("IPv6: ", psutil.net_if_addrs()[interface][1][1])
    print("MAC: ", psutil.net_if_addrs()[interface][0][2])
    print("Bytes recebidos: ", psutil.net_io_counters(pernic=True)[interface].bytes_recv)
    print("Bytes enviados: ", psutil.net_io_counters(pernic=True)[interface].bytes_sent)

def  get_process_consumption(pid):
    """
    Função que retorna o consumo de um processo
    :param pid:
    :return:
    """
    # Lista consumo de memória e cpu
    print("Memória: ", round((psutil.Process(pid).memory_info().rss))/(1024*1024), "MB")
    print("CPU: ", psutil.Process(pid).cpu_percent(), "%")
    print(psutil.Process(pid).cpu_times())

def main_loop():
    """
    Função que executa o programa
    :return:
    """
    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    # Cria o scheduler
    scheduler = sched.scheduler(time.time, time.sleep)
    # Cria o loop
    scheduler.enter(1, 1, list_processes, ())
    scheduler.enter(2, 1, list_processes_by_name, ("python3",))
    # Executa o loop
    scheduler.run()
    end = time.time()
    print("Finalizando as chamadas escalonadas.")
    total = abs(end - start)
    print(f"Tempo total: {total:.0f} segundos")

def menu():
    """
    Função que exibe o menu
    :return:
    """
    print("""
    1 - Listar arquivos de um diretório
    2 - Listar permissões de um arquivo
    3 - Listar processos por nome
    4 - Verificar consumo de um processo
    5 - Executar chamadas escalonadas
    6 - Listar todos os processos
    7 - Listar interfaces de rede disponíveis
    8 - Listar informações da interface de rede
    9 - Listar portas disponíveis por IP
    10 - Obter subnet por IP
    11 - Scannear dispositivos na rede
    12 - Obter consumo de recursos de rede
    13 - Obter consumo de recursos por processo
    15 - Sair
    """)

def main():
    """
    Função principal
    :return:
    """
    menu()
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                dir = input("Digite o diretório: ")
                print(list_dir_files(dir))
            elif choice == 2:
                file = input("Digite o caminho completo do arquivo: ")
                print(list_permissions(file))
            elif choice == 3:
                name = input("Digite o nome do processo: ")
                list_processes_by_name(name)
            elif choice == 4:
                pid = int(input("Digite o PID do processo: "))
                list_resources_by_process(pid)
            elif choice == 5:
                main_loop()
            elif choice == 6:
                list_processes()
            elif choice == 7:
                list_all_network_interfaces()
            elif choice == 8:
                interface = input("Digite a interface: ")
                list_network_info(interface)
            elif choice == 9:
                ip = input("Digite o IP: ")
                list_port_by_ip_using_nmap(ip)
            elif choice == 10:
                ip = input("Digite o IP: ")
                get_subnet_from_ip(ip)
            elif choice == 11:
                subnet = input("Digite a subnet (por exemplo: 192.168.1.0/24): ")
                scan_devices_in_network(subnet)
            elif choice == 12:
                interface = input("Digite a interface: ")
                get_interface_consumption(interface)
            elif choice == 13:
                pid = int(input("Digite o PID do processo: "))
                get_process_consumption(pid)
            elif choice == 15:
                sys.exit()
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")

if __name__ == "__main__":
    sys.exit(main())