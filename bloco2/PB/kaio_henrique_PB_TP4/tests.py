import pygame
import psutil
import cpuinfo
import os, time,subprocess

# Mostra informaçoes de um diretorio
def mostra_diretorio():
    lista = os.listdir()
    dic = {}

    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(os.stat(i).st_size)
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)

    titulo = '{:11}'.format("Tamanho")
    titulo += '{:27}'.format("Data de Modificaçao")
    titulo += '{:27}'.format("Data de Criaçao")
    titulo += "Nome"
    print(titulo)

    for i in dic:
        kb = dic[i][0]/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb))+" KB")
    print(tamanho, time.ctime(dic[i][2]), time.ctime(dic[i][1]), " ", i)

# Mostra informaçoes de um processo
def info_processos():
    # Apenas cria um processo (calculadora) para testar
    pid = subprocess.Popen("bc").pid
    p = psutil.Process(pid)
    print("Nome:", p.name())
    print("Executável:", p.exe())
    print("Tempo de criação:", time.ctime(p.create_time()))
    print("Tempo de usuário:", p.cpu_times().user, "s")
    print("Tempo dte sistema:", p.cpu_times().system, "s")
    print("Percentual de uso de CPU:", p.cpu_percent(interval=1.0), "%")
    perc_mem = '{:.2f}'.format(p.memory_percent())
    print("Percentual de uso de memória:", perc_mem, "%")
    # RSS: Resident set size e VMS: Virtual Memory Size
    mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
    print("Uso de memória:", mem, "MB")
    print("Número de threads:", p.num_threads())

# Mostra texto de acordo com uma chave:
def mostra_texto(s1, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    s1.blit(text, (10, pos_y))
    if chave == "freq":
        freq = psutil.cpu_freq()
        if freq:
            s = freq.current
        else:
            s = "unknown"
        #s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    elif chave == "ip":
        dic_interfaces = psutil.net_if_addrs()
        s = str(dic_interfaces['ens33'][0].address)
    elif chave == "arq":
        s = str(os.listdir('.'))
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, cinza)
    s1.blit(text, (220, pos_y))

# Obtém informações da CPU
info_cpu = cpuinfo.get_cpu_info()

# Mostra as informações de CPU escolhidas + IP:
def mostra_info_cpu():
    s1.fill(branco)
    mostra_texto(s1, "Nome:", "brand", 10)
    mostra_texto(s1, "Arquitetura:", "arch", 30)
    mostra_texto(s1, "Palavra (bits):", "bits", 50)
    mostra_texto(s1, "Frequência (MHz):", "freq", 70)
    mostra_texto(s1, "Núcleos (físicos):", "nucleos", 90)
    mostra_texto(s1, "IP(ens33):", "ip", 110)
    mostra_texto(s1, "Arquivos:", "arq", 130)

    tela.blit(s1, (0, 0))

# Mostrar uso de CPU:
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela #- 2*20
    s5 = pygame.surface.Surface((larg, altura_tela/3))
    pygame.draw.rect(s5, azul, (20, 50, larg, 70))
    larg = larg*capacidade/100
    s6 = pygame.surface.Surface((larg, altura_tela/3))
    pygame.draw.rect(s6, amarelo, (20, 50, larg, 70))
    tela.blit(s5, (0, 370))
    tela.blit(s6, (0, 370))
    text = font.render("Uso de CPU 1:", 1, branco)
    tela.blit(text, (10,370))

    capacidade = psutil.cpu_percent(interval=1)
    larg = largura_tela #- 2*20
    s7 = pygame.surface.Surface((larg, altura_tela/3))
    pygame.draw.rect(s7, azul, (20, 50, larg, 70))
    larg = larg*capacidade/100
    s8 = pygame.surface.Surface((larg, altura_tela/3))
    pygame.draw.rect(s8, amarelo, (20, 50, larg, 70))
    tela.blit(s7,(0, 490))
    tela.blit(s8, (0, 490))
    text = font.render("Uso de CPU 2:", 1, branco)
    tela.blit(text, (10, 490))

def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela #- 2*20
    s3 = pygame.surface.Surface((larg, altura_tela/10))
    pygame.draw.rect(s3, azul, (20, 50, larg, 70))
    larg = larg*disco.percent/100
    s4 = pygame.surface.Surface((larg, altura_tela/10))
    pygame.draw.rect(s4, vermelho, (20, 50, larg, 70))
    tela.blit(s3, (0, 250))
    tela.blit(s4, (0, 250))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (10, 255))

# Mostar uso de memória
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela #- 2*20
    s1 = pygame.surface.Surface((larg, altura_tela/10))
    pygame.draw.rect(s1, azul, (20, 50, larg, 70))
    larg = larg*mem.percent/100
    s2 = pygame.surface.Surface((larg, altura_tela/10))
    pygame.draw.rect(s2, vermelho, (20, 50, larg, 70))
    tela.blit(s1, (0, 130))
    tela.blit(s2, (0, 130))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (10, 130))

# Iniciando a janela principal
largura_tela = 1600
altura_tela = 1200
# Superfície para mostrar as informações:
s1 = pygame.surface.Surface((largura_tela, altura_tela))
s = pygame.surface.Surface((largura_tela, altura_tela))
pygame.font.init()
font = pygame.font.Font(None, 32)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de Recursos")
pygame.display.init()

# Cores:
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 53)

# Cria relógio
clock = pygame.time.Clock()
# Contador de tempo
cont = 60

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    # Fazer a atualização a cada segundo:
    if cont == 60:
        mostra_info_cpu()
        mostra_uso_memoria()
        mostra_uso_disco()
        mostra_uso_cpu()
        cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

mostra_diretorio()
info_processos()