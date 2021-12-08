import time

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1): # start, stop and step
    fat = fat * i
  return(fat)

vetorB = []
def fatorialB(lista):
  for i in lista:
    resultado = fatorial(i)
    vetorB.append(resultado)

lista = [5,5,5]

time0 = time.time()
fatorialB(lista)
timeFinal = time.time()
print(vetorB)
print('Tempo decorrido = ' + str(float(timeFinal) - float(time0)) + ' segundos')