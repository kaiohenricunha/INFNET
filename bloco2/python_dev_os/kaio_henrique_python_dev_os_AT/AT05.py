# path = os.getcwd()
# dir = '/bloco2/python_dev_os/kaio_henrique_python_dev_os_AT'
# path_dir = path + dir
# os.chdir(path_dir)
list_a, list_b, soma = [], [], []
try:
    file_a = open('a.txt', 'r', encoding='utf-8')
    file_b = open('b.txt', 'r', encoding='utf-8')
    cont_a = file_a.readlines() # returns a list containing each line in the file as a list item
    cont_b = file_b.readlines()
    file_a.close()
    file_b.close()
    for a in cont_a:
        list_a.append(int(a.strip())) # removes any spaces
    for b in cont_b:
        list_b.append(int(b.strip()))
    while len(list_a)!=len(list_b): # verifica se as listas tem o mesmo tamanho
        if len(list_a)<len(list_b):
            list_a.append(0) # add 0 to the empty spaces of list_a
        else:
            list_b.append(0)       
    for i in range(0,len(list_a)):
        soma.append(list_a[i]+list_b[i])   
    print("\nLISTA A: ",*list_a) # * removes the brackets
    print("+")
    print("LISTA B: ",*list_b)
    print("----------------------------------------")
    print("SOMA =  ",*soma, "\n")
except FileNotFoundError:
    print("\nArquivo não encontrado!\n")
    print("Verifique se está no path correto...\n")
except Exception as erro:
    print("\nErro: ", erro)