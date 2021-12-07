import os, time

soma = 0
directory = os.getcwd() # returns the current working directory
if os.path.isdir(directory):
    path = os.walk(directory)
    print(path)
    for root, dirs, files in path:
        path = root.split(os.sep)
        print("-------------------------------------")
        print("Nome do diretório:",os.path.basename(root))
        #dic = input("Entre com o nome do diretório que deseja salvar")
        #print("Nome do diretório:",dic)
        print("-------------------------------------")
        time.sleep(0.5)
        for file in files:
            print("\t", file)
            soma += os.stat(os.path.join(root, file)).st_size
            print("-------------------------------------")
    print("Total de bytes:", soma)
    print()   
else:
    print("O diretório", directory, "não existe.")