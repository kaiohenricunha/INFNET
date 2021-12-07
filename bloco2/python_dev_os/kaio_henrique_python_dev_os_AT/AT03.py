import os, time

soma = 0
directory = os.getcwd() # returns the current working directory
if os.path.isdir(directory):
    path = os.walk(directory) # generates the file names in a directory tree
    for root, dirs, files in path:
        path = root.split(os.sep)
        print("======================================")
        print("Diretório:",os.path.basename(root))
        print("======================================")
        time.sleep(1)
        for file in files:
            print("\t", file)
            soma += os.stat(os.path.join(root, file)).st_size
    print("Total de bytes:", soma)
    print()   
else:
    print("O diretório", directory, "não existe.")