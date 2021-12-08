import os, time

soma = 0
directory = os.getcwd() # returns the current working directory
if os.path.isdir(directory): # checks if the path is a directory
    path = os.walk(directory) # returns an object with all the files in the directory
    for root, dirs, files in path: # root is the path, dirs is the list of directories, files is the list of files
        path = root.split(os.sep) # returns a list of all the directories in the path by using the separator
        print("======================================")
        print("Diretório:",os.path.basename(root))
        print("======================================")
        time.sleep(1)
        for file in files: 
            print("\t", file)
            soma += os.stat(os.path.join(root, file)).st_size # returns the size of the file
    print("Total de bytes:", soma)
    print()   
else:
    print("O diretório", directory, "não existe.")