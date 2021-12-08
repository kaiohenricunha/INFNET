import pickle, socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp.connect((socket.gethostname(), 8881))

    mensagem = input('Escreva o caminho do diretório: ')
    tcp.send(mensagem.encode('UTF-8'))

    bytes = tcp.recv(4096)
    resposta = pickle.loads(bytes)

    for item in resposta:
        print(item)

    mensagem = 'fim'
    tcp.send(mensagem.encode('UTF-8'))

except Exception as erro:
    print(str(erro))

tcp.close()

input("Pressione qualquer tecla para sair...")

# path para testes: bloco2/python_dev_os/kaio_henrique_python_dev_os_AT/AT06-client.py