import socket

TCP_IP = "127.0.0.1" #define o ip
FILE_PORT = 5005 #define a porta
DATA_PORT = 5006 #define a porta
timeout = 3
buf = 1024 #define o tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket, define como ipv4 e TCP
sock_f.bind((TCP_IP, FILE_PORT)) #informa ao SO que iremos usar os respectivos Ip e Porta
sock_f.listen(1) #faz com que o servidor permita novas conexoes

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket, define como ipv4 e TCP
sock_d.bind((TCP_IP, DATA_PORT)) #informa ao SO que iremos usar os respectivos Ip e Porta
sock_d.listen(1) #faz com que o servidor permita novas conexoes


while True:
    conn, addr = sock_f.accept() #capta a coneçao e endereço
    data = conn.recv(buf)
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb')

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    print "%s Finish!" % file_name
    f.close()