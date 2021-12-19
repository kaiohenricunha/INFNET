# Testei as 3 opções de execução com um vetor de mesmo tamanho, 10, e obtive os seguintes resultados:
# multithreading: 0.0025725364685058594 segundos
# multiprocessing: 4.051970481872559 segundos
# sequencial: 5.340576171875e-05 segundos
# A execuçao serial foi mais lentar pois executa os processos em sequencia, 
# enquanto que a execuçao com threads executa os processos em paralelo.
# A diferença entre multiprocessing e multithreading é que o multiprocessing tem um espaço de memória separado,
# enquanto que o multithreading tem espaço de memória compartilhado.

import random, time, threading

class Threading():

    def __init__(self): # Construtor da classe Threading que recebe o número de threads e o tamanho do vetor
        self.vetor_size = int(input("Digite o tamanho do vetor: "))
        self.vetor_A = []
        self.vetor_B = []
        self.thread_list = []
        self.thread_num = 4
        self.thread_task()

    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def calcFatorial(self, a_list, start, end):
        for item in a_list[start:end]:
            factorial = self.fatorial(item)
            self.vetor_B.append(factorial)

    def thread_task(self):
        start_time = float(time.time())

        for i in range(self.vetor_size):
            self.vetor_A.append(random.randint(0, self.vetor_size))

        self.list_size = len(self.vetor_A)

        for i in range(self.thread_num): # Criação de threads
            start = i * int(self.list_size/self.thread_num) # Define o início da lista de cada thread
            end = (i + 1) * int(self.list_size/self.thread_num) # Define o fim da lista de cada thread
            t = threading.Thread(target=self.calcFatorial, args=(self.vetor_A, start, end)) # Criação de uma thread
            t.start()
            self.thread_list.append(t)

        for t in self.thread_list:
            t.join()

        end_time = float(time.time())
        print('{}Tempo decorrido: {} segundos'.format(' '*2, end_time - start_time))

Threading() # Instanciando a classe