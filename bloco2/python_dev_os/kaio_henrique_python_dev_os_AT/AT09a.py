# Testei as 3 opções de execução com um vetor de mesmo tamanho, 10, e obtive os seguintes resultados:
# multithreading: 0.0025725364685058594 segundos
# multiprocessing: 4.051970481872559 segundos
# sequencial: 5.340576171875e-05 segundos
# A execuçao serial foi mais lentar pois executa os processos em sequencia, 
# enquanto que a execuçao com threads executa os processos em paralelo.
# A diferença entre multiprocessing e multithreading é que o multiprocessing tem um espaço de memória separado,
# enquanto que o multithreading tem espaço de memória compartilhado.

import time
import random

class Sequencial():

    def __init__(self):
        self.vetor_size = int(input("Digite o tamanho do vetor: "))
        self.vetor_A = []
        self.vetor_B = []
        
    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def calc_factorial(self): # Calcula o fatorial de um número e armazena em um vetor A

        self.start_time = float(time.time())

        for i in range(self.vetor_size):
            self.vetor_A.append(random.randint(0, self.vetor_size)) # generates a random number between 0 and self.vetor_size

        for item in self.vetor_A:
            sq_factor = self.fatorial(item) # calculates the factorial of the vector
            self.vetor_B.append(sq_factor)

        self.end_time = float(time.time())

    def print_result(self):
        self.calc_factorial()
        print('{}Tempo decorrido: {} segundos'.format(' '*2, self.end_time - self.start_time))


Sequencial().print_result() # instancia a classe Sequencial e chama o método print_result()