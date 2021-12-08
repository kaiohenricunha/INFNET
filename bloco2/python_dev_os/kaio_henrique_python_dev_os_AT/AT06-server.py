import os, pickle, socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 8881
tcp.bind((host, porta))
tcp.listen()

(socket_cliente, addr) = tcp.accept()
print("Conectado a:", str(addr))

response = []
while True:
    mensagem = socket_cliente.recv(4096)
    diretorio = mensagem.decode('UTF-8')

    if diretorio != 'fim': # Se não for o fim, continua.
        for arquivo in os.listdir(diretorio):
            if os.path.isfile(diretorio + '//' + arquivo):
                response.append(arquivo)

        bytes = pickle.dumps(response)
        socket_cliente.send(bytes)

    else:
        break

socket_cliente.close()

input("Pressione qualquer tecla para sair...")