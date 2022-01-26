import socket
import sys

TCP_IP = "127.0.0.1" #define o ip
FILE_PORT = 5005 #define a porta
DATA_PORT = 5006 #define a porta
buf = 1024 #define o tamanho do buffer
file_name = sys.argv[1] #define o nome do arquivo


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket, define como ipv4 e TCP
    sock.connect((TCP_IP, FILE_PORT))  #possibilita conexao do servidor
    sock.send(file_name) #envia arquivo
    sock.close() #finaliza socket

    print "Sending %s ..." % file_name #printa mensagem

    f = open(file_name, "rb") #apre arquivo e le
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket, define como ipv4 e TCP
    sock.connect((TCP_IP, DATA_PORT)) #possibilita conexao do servidor
    data = f.read() #realiza leitura
    sock.send(data) #envia socket

finally:
    sock.close() #fecha o socket
    f.close()