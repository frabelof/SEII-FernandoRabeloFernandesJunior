import socket
import threading
import time

PORT = 5050 #define a porta
FORMATO = 'utf-8' #define o formato
SERVER = "192.168.0.109" #define o IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) #conecta

def handle_mensagens(): #gerencia as mensagens que tem no servidor
    while(True): #loope para aceitar nova mensagem
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO)) #envia mensagem

def enviar_mensagem():
    mensagem = input() #pede ao cliente inserir sua mensagem
    enviar("msg=" + mensagem) #envia mensagem

def enviar_nome():
    nome = input('Digite seu nome: ') #pede ao cliente para inserir seu nome
    enviar("nome=" + nome) #envia nome

def iniciar_envio():
    enviar_nome() #envia nome
    enviar_mensagem() #envia mensagem

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start() #inicia thread 1
    thread2.start() #inicia thread 2

iniciar()