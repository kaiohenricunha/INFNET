import pygame
import psutil

pygame.font.init()
font = pygame.font.Font(None, 32)

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de Recursos")
pygame.display.init()

preto = (0, 0, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)

# Mostar uso de memória
def mostra_uso_memoria():
    
    #busca o valor da memória em uso
    mem = psutil.virtual_memory()
    #define a largura da barra azul/vermelha
    larg = largura_tela - 2*20
    #define a cor de fundo da tela: preto
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    #muda o valor da variável larg para representar a porcentagem utilizada
    larg = larg*mem.percent/100
    #cria a tarja vermelha, que vai depender do tamanho de larg
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    #calcula e arredonda o uso de memória total
    total = round(mem.total/(1024*1024*1024),2)
    #exibe o valor utilizado de memória(total)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    #define o texto da barra com uma string que informa o total de memória utilizada
    text = font.render(texto_barra, True, branco)
    #exibe o texto devidamente posicionado e formatado
    tela.blit(text, (20, 10))

# Mostrar o uso de disco local
def mostra_uso_disco():
    
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg*disco.percent/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, True, branco)
    tela.blit(text, (20, 10))

# Mostrar uso de CPU:
def mostra_uso_cpu():
    
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    text = font.render("Uso de CPU:", True, branco)
    tela.blit(text, (20, 10))


# Cria relógio
clock = pygame.time.Clock()

cont = 60

terminou = False

while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    # Fazer a atualização a cada segundo:
    if cont == 60:
        mostra_uso_cpu()
        cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

    # Finaliza a janela
pygame.display.quit()



