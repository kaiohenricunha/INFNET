from queue import Empty
import pygame, psutil, cpuinfo, platform, os, time, sched

#---------------------------------------------------------------------------------------------------#
# Quarta Entrega do Projeto de Bloco 

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

#---------------------------------------------------------------------------------------------------#
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

#---------------------------------------------------------------------------------------------------#
# Função que irá fazer o agendamento, escalonamento e contar o tempo real e o tempo do clock de 2 funções do programa
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

#---------------------------------------------------------------------------------------------------#

def mostra_titulo():
        tela.blit(s1, (0,s1_posicao))
        texto_titulo = "Monitoramento e Análise do Computador"
        font = pygame.font.Font(None, 30)
        text = font.render(texto_titulo, 1, gold)
        s1.blit(text, (100, 14))

def uso_memoria():     
        mem = psutil.virtual_memory()
        
        larg = largura_tela - 2*20
        pygame.draw.rect(s2,cinzaclaro, (20, 40, larg, 40))
        tela.blit(s2, (0,s2_posicao))
        
        larg = larg*mem.percent/100
        pygame.draw.rect(s2, cornFlowerBlue, (20, 40, larg, 40))
        tela.blit(s2, (0,s2_posicao))
        
        total = round(mem.total/(1024*1024*1024),2)
        texto_memoria = "Uso de Memória (Total: " + str(total) + "GB):"
        text = font.render(texto_memoria, 1, branco)
        s2.blit(text, (20, 10))
        
def uso_disco():
        disco = psutil.disk_usage('.')
        
        larg = largura_tela - 2*20    
        pygame.draw.rect(s3, cinzaclaro, (20, 40, larg, 40))
        tela.blit(s3, (0, s3_posicao))
        
        larg = larg*disco.percent/100
        pygame.draw.rect(s3, verde, (20, 40, larg, 40))
        tela.blit(s3, (0, s3_posicao))
        
        total = round(disco.total/(1024*1024*1024), 2)
        texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
        text = font.render(texto_barra, 1, branco)
        s3.blit(text, (20, 10))

def mostra_info_cpu():                    
        mostra_texto(s4, "Nome Processador:", "brand_raw", 10)
        mostra_texto(s4, "Arquitetura:", "arch", 30)
        mostra_texto(s4, "Palavra (bits):", "bits", 50)
        mostra_texto(s4, "Frequência (MHz):", "freq", 70)
        mostra_texto(s4, "Núcleos (físicos):", "nucleos", 90)
        tela.blit(s4, (0, s4_posicao))  
        
def mostra_texto(surface, nome, chave, pos_y):
        text = font.render(nome, True, branco)
        surface.blit(text, (20, pos_y))
        if chave == "freq":
                resultado = str(round(psutil.cpu_freq().current, 2))
        elif chave == "nucleos":
                resultado = str(psutil.cpu_count())
                resultado = resultado + " (" + str(psutil.cpu_count(logical=False)) + ")"
        else:
                resultado = str(info_cpu[chave])
        text = font.render(resultado, True, branco)
        surface.blit(text, (190, pos_y))

def mostra_uso_cpu(surface, l_cpu_percent):           
        num_cpu = len(l_cpu_percent)  #Quantidade de núcleos
        x = y = 10
        espacos = 10
        alt = surface.get_height() - 2*y -120 #Pega a altura da surface e diminui 10 pixels em cima e embaixo
        larg = (surface.get_width() - 2*y - (num_cpu+1)*espacos)/num_cpu
        bordas_laterais = x + espacos
        for i in l_cpu_percent:
                pygame.draw.rect(surface, vermelho, (bordas_laterais, 120, larg, alt))
                pygame.draw.rect(surface, cinzaclaro, (bordas_laterais, 120, larg, (1-i/100)*alt))
                bordas_laterais = bordas_laterais + larg + espacos
        
def plataforma():
        plat_processor = platform.processor()
        plat_node = platform.node()
        plat_platform = platform.platform()
        plat_system = platform.system()

        tela.blit(s5, (0, s5_posicao))
        
        texto_processor = '{:30}'.format("Família do processador:") + str(plat_processor)
        text = font.render(texto_processor, True, branco)
        s5.blit(text, (20, 8))
        
        texto_node = '{:30}'.format("Nome do computador:") + str(plat_node)
        text = font.render(texto_node, True, branco)
        s5.blit(text, (20, 28))
        
        texto_platform = '{:30}'.format("Plataforma:") + str(plat_platform)
        text = font.render(texto_platform, True, branco)
        s5.blit(text, (20, 48))
        
        texto_system = '{:30}'.format("Sistema Operacional:") + str(plat_system)
        text = font.render(texto_system, True, branco)
        s5.blit(text, (20, 68))

def ip():
        dic_interfaces = psutil.net_if_addrs()
        ip_maquina = dic_interfaces['Conexão Local'][1].address
        
        tela.blit(s6, (0, s6_posicao))
        
        texto_barra1 = '{:30}'.format("Número de IP da Máquina:") + str(ip_maquina)
        text = font.render(texto_barra1, 1, branco)
        s6.blit(text, (20, 15))

# OBTENDO INFORMAÇÕES DA CPU
info_cpu = cpuinfo.get_cpu_info()

# CORES:
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 230)
verde = (60, 179, 113)
cornFlowerBlue = (100,149,237)
cinzaclaro = (192,192,192)
cinzaescuro = (35,35,35)
gold = (255,215,0)

# INICIANDO E DEFININDO TAMANHO DA FONTE
pygame.font.init()
font = pygame.font.Font(None, 23)

# INICIANDO A JANELA PRINCIPAL
largura_tela = 600
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("DR5 Projeto - Teste de Performance 5")
pygame.display.init()

# SURFACES: DEFINIR PORCENTAGEM DA TELA E CALCULANDO ALTURA DA SURFACE
s1_altura = int(0.06 * altura_tela)
s2_altura = int(0.12 * altura_tela)
s3_altura = int(0.12 * altura_tela)
s4_altura = int(0.52 * altura_tela)
s5_altura = int(0.12 * altura_tela)
s6_altura = int(0.06 * altura_tela)

# SURFACES: DEFININDO POSIÇÃO NA TELA 
# (uma surface começa na posição que termina a surface anterior)
s1_posicao = 0
s2_posicao = s1_altura
s3_posicao = s1_altura + s2_altura
s4_posicao = s1_altura + s2_altura + s3_altura
s5_posicao = s1_altura + s2_altura + s3_altura + s4_altura
s6_posicao = s1_altura + s2_altura + s3_altura + s4_altura + s5_altura

# SURFACES: CRIANDO 6 SURFACES E DEFININDO AS CORES
s1 = pygame.surface.Surface((largura_tela, s1_altura))
s1.fill(cinzaescuro)
s2 = pygame.surface.Surface((largura_tela, s2_altura))
s2.fill(cinzaescuro)
s3 = pygame.surface.Surface((largura_tela, s3_altura))
s3.fill(cinzaescuro)
s4 = pygame.surface.Surface((largura_tela, s4_altura))
s4.fill(cinzaescuro)
s5 = pygame.surface.Surface((largura_tela, s5_altura))
s5.fill(cinzaescuro)
s6 = pygame.surface.Surface((largura_tela, s6_altura))
s6.fill(cinzaescuro)

# CRIA RELÓGIO
clock = pygame.time.Clock()

# CONTADOR DE TEMPO
cont = 60

# LOOP
terminou = False
while not terminou:        
        # VERIFICA OS EVENTOS DO MOUSE:
        for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                        terminou = True
                
        # ATUALIZA A TELA QUANDO O CONTADOR CHEGA EM 60:
        if cont == 60:
                mostra_titulo()
                uso_memoria()
                uso_disco()
                mostra_info_cpu()
                mostra_uso_cpu(s4, psutil.cpu_percent(interval=2, percpu=True))
                plataforma()
                ip()
                cont = 0

        # ATUALIZA O DESENHO NA TELA
        pygame.display.update()

        # 60 FRAMES POR SEGUNDO
        clock.tick(60)
        cont = cont + 1

# FINALIZA O PYGAME
pygame.display.quit()