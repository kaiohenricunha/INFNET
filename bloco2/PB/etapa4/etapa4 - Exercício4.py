import os
lista = os.listdir()
dic_arq = {} # Usar dicionário para guardar os arquivos por tipo
for i in lista:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1] # Separa em nome e extensão
        # Verifica se a extensão está presente no dicionário:
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i) # Usa a extensão como chave

print(dic_arq)