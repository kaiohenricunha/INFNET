# Testei as 3 opções de execução com um vetor de mesmo tamanho, 10, e obtive os seguintes resultados:
# multithreading: 0.0025725364685058594 segundos
# multiprocessing: 4.051970481872559 segundos
# sequencial: 5.340576171875e-05 segundos
# A execuçao serial foi mais lentar pois executa os processos em sequencia, 
# enquanto que a execuçao com threads executa os processos em paralelo.
# A diferença entre multiprocessing e multithreading é que o multiprocessing tem um espaço de memória separado,
# enquanto que o multithreading tem espaço de memória compartilhado.

import multiprocessing, sys, time, random

vector = []
vector_result = []

output = multiprocessing.Queue()

def factorial(n):
    f = n
    for i in range(n-1,1,-1):
        f = f * i
    return(f)

def append_processing(vector, factorial, vector_result, output):
    for n in vector:
        output.put(factorial(n))

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def running_process():

    try:

        n = int(input("Digite o tamanho do vetor: "))
        for i in range (n):
            vector.append(random.randint(0,100))

        size = len(vector)


        process_0 = multiprocessing.Process(target=append_processing, args=(vector[0:1], factorial, vector_result, output))
        process_0.start()

        process_1 = multiprocessing.Process(target=append_processing, args=(vector[1:2], factorial, vector_result, output))
        process_1.start()

        process_2 = multiprocessing.Process(target=append_processing, args=(vector[2:3], factorial, vector_result, output))
        process_2.start()

        process_3 = multiprocessing.Process(target=append_processing, args=(vector[3:size], factorial, vector_result, output))
        process_3.start()

        while len(vector) != len(vector_result):
            vector_result.append(output.get())

        process_0.join()
        process_1.join()
        process_2.join()
        process_3.join()
    except Exception as e:
        print("Error: {}".format(e))

def main():
    print("\nExecutando multiprocessing...")
    print("Tempo decorrido: {} segundos".format(calculate_time(running_process)))
    print("\n")

if __name__ == "__main__":
    sys.exit(main())