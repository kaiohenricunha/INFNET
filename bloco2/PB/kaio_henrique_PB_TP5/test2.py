from queue import Empty
import pygame, psutil, cpuinfo, platform, os, time, sched

#---------------------------------------------------------------------------------------------------#
# Função que irá fazer o agendamento, escalonamento e contar o tempo real e o tempo do clock de 2 funções do programa

def lista_arquivos(lista_arq_dir):
        time.sleep(5)
        for i in lista_arq_dir:
                i = os.path.join(caminho, i)
                if os.path.isfile(i):
                        lista_arq.append(i)
                else:
                        lista_dir.append(i)

        dic_arq = {}  # cria um dicionário
        for i in lista_arq:  # Percorre a lista de arquivos e diretórios
                dic_arq[i] = []  # Cria uma lista para cada arquivo
                dic_arq[i].append(os.stat(i).st_ctime) # Tempo de criação
                dic_arq[i].append(os.stat(i).st_size) # Tamanho em Bytes
                
        print("----------INFORMAÇÕES SOBRE ARQUIVOS E DIRETÓRIOS----------\n")    
        titulo = '{:27}'.format("Data de Criação")  
        titulo = titulo + '{:13}'.format("Tamanho")
        titulo = titulo + "Nome"
        print(titulo)

        if dic_arq is not Empty:
                for i in dic_arq:
                        kb = dic_arq[i][1]/1024
                        tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + "KB"))
                        print(time.ctime(dic_arq[i][0]), " ",tamanho, " ", i)
        print("")

        if len(lista_dir) > 0:
                print("Diretórios localizados:")
                for i in lista_dir:
                        print('\t'+i)

        tempo_fim = time.time()
        global duracao_lista_arquivos
        duracao_lista_arquivos = tempo_fim - inicio    

caminho = input("Digite o caminho do diretório: ")
lista_arq_dir = os.listdir(caminho)
lista_arq = []
lista_dir = []


def scheduler():        
        scheduler = sched.scheduler(time.time, time.sleep)
        global inicio
        inicio = time.time()
        inicio_form = time.ctime()

        scheduler.enter(2, 1, lista_arquivos, (lista_arq_dir,))
        clock_lista = time.process_time()
        scheduler.run()

        scheduler.enter(3, 1, mostra_processos, (pids,))
        clock_mostra = time.process_time()
        scheduler.run()

        print("---------- COMPARANDO TEMPO DE EXECUÇÃO E TEMPO DO CLOCK DAS FUNÇÕES AGENDADAS----------\n")
        print("Início da contagem: ", inicio_form, "\n")
        print("Duração da função lista_arquivos(): ", '{:.2f}'.format(duracao_lista_arquivos), "segundos. Tempo do clock: ", '{:.2f}'.format(clock_lista),"\n")
        print("Duração da função mostra_processos(): ", '{:.2f}'.format(duracao_mostra_processos), "segundos. Tempo do clock: ", '{:.2f}'.format(clock_mostra),"\n")
        print("Fim da contagem: ", time.ctime(), "\n")

scheduler()

def mostra_processos(pids):
        time.sleep(5)
        for i in pids:
                try:
                        processo = psutil.Process(i) 
                        dic_proc[i] = []
                        dic_proc[i].append(processo.pid)
                        dic_proc[i].append(processo.status())
                        dic_proc[i].append(processo.num_threads())        
                        dic_proc[i].append(processo.name())       
                except:
                        pass

        print("\n----------INFORMAÇÕES SOBRE PROCESSOS DO SISTEMA----------\n")
        titulo = '{:8}'.format("PID:")  
        titulo = titulo + '{:12}'.format("Status:")
        titulo = titulo + '{:12}'.format("Threads:")
        titulo = titulo + "Nome:"
        print(titulo)

        for i in dic_proc:
                print('{:7}'.format(str(dic_proc[i][0])),'{:11}'.format(str(dic_proc[i][1])),'{:11}'.format(str(dic_proc[i][2])),dic_proc[i][3])
        
        tempo_fim = time.time()
        global duracao_mostra_processos
        duracao_mostra_processos = tempo_fim - inicio

pids = psutil.pids()
dic_proc = {}