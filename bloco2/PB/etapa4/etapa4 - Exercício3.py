import os
lista = os.listdir()
lista_arq = [] # lista para guardar os arquivos
lista_dir = [] # lista para guardar os diretórios
for i in lista:
    if os.path.isfile(i):
        lista_arq.append(i)
    else:
        lista_dir.append(i)

if len(lista_arq) > 0: # Checa se tem arquivo na lista
    print("Arquivos:")
    for i in lista_arq:
        print("\t"+i) # insere uma tabulação no início
    print("") # Quebra de linha
    
if len(lista_dir) > 0: # Checa se tem diretório na lista
    print("Diretórios:")
    for i in lista_dir:
        print("\t"+i) # insere uma tabulação no início
    print("") # Quebra de linha