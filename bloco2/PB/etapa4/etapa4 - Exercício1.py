import os
# Obtém lista de arquivos e diretórios do diretório corrente:
lista = os.listdir()
dic = {} # cria dicionário
for i in lista: # Varia na lista dos arquivos e diretórios
    if os.path.isfile(i): # checa se é um arquivo
        # Cria uma lista para cada arquivo. Esta lista contém o
        # tamanho, data de criação e data de modificação.
        dic[i] = []
        dic[i].append(os.stat(i).st_size) # Tamanho
        dic[i].append(os.stat(i).st_atime) # Tempo de criação
        dic[i].append(os.stat(i).st_mtime) # Tempo de modificação
