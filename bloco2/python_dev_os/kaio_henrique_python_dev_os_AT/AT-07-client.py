import pickle, socket

def motrar_dados(dado):
    # dado['mem_total'] = dado['mem_total'] / (1024 * 1024)
    
    print(f""" 
    memoria total: {dado['mem_total'] / (1024 * 1024):.2f} MB,
    memoria livre: {dado['mem_disp'] / (1024 * 1024):.2f} MB,
    """)

    # print(f""" 
    # memoria total: {dado['mem_total']},
    # memoria disponível: {dado['mem_disp']}
    # """)

host = socket.gethostname()
porta = 9999

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HP = (host, porta)
msg = ' '
envia = msg.encode('UTF-8')

for i in range(4):
    if i == 3:
        msg = 'memoria'
        envia = msg.encode('UTF-8')
    udp.sendto(envia, HP)
    udp.settimeout(5.0)
    try:
        (msg_serv, HP) = udp.recvfrom(1024)
        resposta = pickle.loads(msg_serv)
        if resposta != '':
            motrar_dados(resposta)
            break
        else:
            print('processando...')
    except Exception as erro:
        print(str(erro))
        input("Pressione qualquer tecla para sair...")
        continue

udp.close()