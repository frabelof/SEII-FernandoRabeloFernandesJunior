import socket
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname()) #define o ip
PORT = 5050 #define a porta
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket, define como ipv4 e TCP
server.bind(ADDR) #informa o SO que iremos usar os respectivos IP e Porta

conexoes = []
mensagens = []

def enviar_mensagem_individual(conexao): #funçao que envia mensagem para uma pessoa
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i] #cria mensagem de envio
        conexao['conn'].send(mensagem_de_envio.encode()) #enviar mensagem
        conexao['last'] = i + 1
        time.sleep(0.2)

def enviar_mensagem_todos(): #funçao que envia mensagem para todos
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr): #funçao que lida com os clientes
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}") #entra novo cliente
    global conexoes
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO) #define tamanho da mensagem
        if(msg):
            if(msg.startswith("nome=")): #identifica se a mensagem é nome
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1] #cliente informa seus dados abaixo
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao)
                enviar_mensagem_individual(mapa_da_conexao)
            elif(msg.startswith("msg=")): #identifica se a mensagem é mensagem
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos() #envia mensagem para todos



def start():
    print("[INICIANDO] Iniciando Socket")
    server.listen() #socket ouve cliente, servidor permite novas conexoes
    while(True):
        conn, addr = server.accept() #cliente entra e é captado a coneçao e endereço do cliente
        thread = threading.Thread(target=handle_clientes, args=(conn, addr)) #cria thread para o cliente
        thread.start() #incia thread

start()