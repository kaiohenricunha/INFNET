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

    def calc_factorial(self):

        self.start_time = float(time.time())

        for i in range(self.vetor_size):
            self.vetor_A.append(random.randint(0, self.vetor_size))

        for item in self.vetor_A:
            sq_factor = self.fatorial(item)
            self.vetor_B.append(sq_factor)

        self.end_time = float(time.time())

    def print_result(self):
        self.calc_factorial()
        print('{}Tempo de processamento: {}'.format(' '*2, self.end_time - self.start_time))


Sequencial().print_result()