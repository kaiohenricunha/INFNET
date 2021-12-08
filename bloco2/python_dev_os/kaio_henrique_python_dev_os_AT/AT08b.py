import threading,time,random

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

vetorB = []
def fatorialB(listaIn,inicio,fim):
  for i in range(inicio,fim):
    holder = fatorial(listaIn[i])
    vetorB.append(holder)
    
threadsNumber = 4

numLista = int(input("Digite o tamanho do vetor(0-20): "))

lista = []
for i in range(numLista):
    lista.append(random.randint(0, 20))

tamanho = len(lista)
metade = int(tamanho//threadsNumber)
treadList = []
time0 = time.time()

for i in range(threadsNumber):
    t = threading.Thread(target=fatorialB,args=(lista,(metade*i),(metade*(i+1))))
    treadList.append(t)
    t.start()
for i in treadList:
    i.join()
timeFinal = time.time()
print(vetorB)
print("Tamanho do vetor",numLista)
print("Número de threads",threadsNumber)
print('Tempo decorrido: ' + str(float(timeFinal) - float(time0)) + ' segundos')