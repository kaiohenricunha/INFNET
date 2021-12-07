import os

path = os.getcwd()
dir = '/bloco2/python_dev_os/kaio_henrique_python_dev_os_AT'
path_dir = path + dir
os.chdir(path_dir)
file = open("queremos-saber.txt", "r")

for line in file:   
    print("\nTEXTO")
    print("----------------")
    print(line, end="")
    print()
    print("\n", "TEXTO REVERSO")
    print("-----------------")
    print(line[::-1])  # start at the end of the string and go backwards  
file.close()

os.chdir(path)