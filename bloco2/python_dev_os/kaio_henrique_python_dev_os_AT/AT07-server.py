import pickle, socket, psutil

host = socket.gethostname()
porta = 9999
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HP = (host, porta)
udp.bind((HP))

mem = psutil.virtual_memory()

while True:
    (msg, cliente) = udp.recvfrom(1024)
    msg_client = msg.decode('UTF-8')

    if msg_client == 'memoria':
        resposta = {
            'mem_total': mem.total,
            'mem_disp': mem.free
        }

        bytes = pickle.dumps(resposta)
        udp.sendto(bytes, cliente)
        break
    else:
        resposta = ''
        bytes = pickle.dumps(resposta)
        udp.sendto(bytes, cliente)

udp.close()