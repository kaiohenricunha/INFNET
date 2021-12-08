import multiprocessing
import time
import random

vetor_B = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calc_fatorial(q1, q2):
    factorial_list = q1.get()
    vetor = []
    for item in factorial_list:
        factorial = fatorial(item)
        vetor.append(factorial)
    q2.put(vetor)


if __name__ == "__main__":

    vetor_size = int(input("Digite o tamanho do vetor(0-20): "))

    start_time = float(time.time())

    vetor_A = []
    for i in range(vetor_size):
        vetor_A.append(random.randint(0, 20)) # adiciona um numero aleatorio ao vetor

    process_number = 4 # numero de processos

    queue_in = multiprocessing.Queue() # cria uma fila de entrada
    queue_out = multiprocessing.Queue() #  cria uma fila de saida

    lista_proc = []
    for i in range(process_number): 
        start = i * int(vetor_size/process_number)
        end = (i + 1) * int(vetor_size/process_number)
        queue_in.put(vetor_size[start:end])
        mp = multiprocessing.Process(target=calc_fatorial, args=(queue_in,
                                                           queue_out))
        mp.start()
        lista_proc.append(m)

    for mp in lista_proc:
        mp.join()

    end_time = float(time.time())
    print('{}Tempo decorrido: {}'.format(' '*2, end_time - start_time))