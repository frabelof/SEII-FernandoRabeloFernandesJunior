import socket
import select

UDP_IP = "127.0.0.1" #define o ip
IN_PORT = 5005 #define a porta
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria socket, define como ipv4 e UDP
sock.bind((UDP_IP, IN_PORT)) #informa ao SO que iremos usar os respectivos Ip e Porta

while True: #recebe o entereço e printa
    data, addr = sock.recvfrom(1024)
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb')

    while True: #verifica se o servidor esta pronto, recebe endereço e caso nao esteja, printa mensagem
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print "%s Finish!" % file_name
            f.close()
            break