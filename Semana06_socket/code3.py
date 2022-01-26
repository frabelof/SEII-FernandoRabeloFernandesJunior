import socket
import time
import sys

UDP_IP = "127.0.0.1" #define o ip
UDP_PORT = 5005 #define a porta
buf = 1024 #define o tamanho do buffer
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria socket, define como ipv4 e UDP
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

f = open(file_name, "r")
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #verifica o IP e a porta UDP
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()