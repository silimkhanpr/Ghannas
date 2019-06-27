from threading import Thread
import datetime
from DatabaseQuery import *
from socket import AF_INET, SOCK_STREAM, socket
from test import server_config,split

#HOST = input("Enter Host IP\n")
HOST = "172.31.4.72"
PORT = 3000 
uname = ""
addresses = {}
clients = {}
eid = {}


#HOSTA = input("Enter Host IP\n")
HOSTA = "172.31.4.72"
PORTA = 4000
BufferSize1 = 4096
addressesa = {}


def AConnections():
    while True:
        try:
            client, addr = serverAudio.accept()
            
            print("{} is connected(audio connection)!!".format(addr))
            addressesa[client] = addr
            Thread(target=ClientConnectionSound, args=(client, )).start()
        except:
            continue


def ClientConnectionSound(client):
    while True:
        try:
            data = client.recv(BufferSize1)
            broadcastSound(client, data)
        except:
            continue

def broadcastSound(clientSocket, data_to_be_sent):
    for client in addressesa:
        if client != clientSocket:
            client.sendall(data_to_be_sent)
    


def Connections():
    while True:
        client, addr = server.accept()
        addr1 = format(addr)
        addr2 = split(addr,2)
        print(addr2)
        print("text connection")
        global uname
        uname, eid[addr2] = emp_ip(addr2)
        print(uname)
        client.send(("Welcome to Chat Room {}.".format(uname)).encode("utf-8"))
        addresses[client] = addr1
        clients[client] = uname
        Thread(target=ClientConnection, args=(client, )).start()


def ClientConnection(client):
    name = clients[client]
    a = addresses[client]
    addr2 = split(a, 2)
    while True:
        msg = client.recv(BufferSize).decode("utf-8")
        if msg != "quit":
            Broadcast(addr2, msg.encode("utf-8"), name+":")
            print(name+":"+msg)
        else:
            client.send(("Will see you soon..").encode("utf-8"))
            del clients[client]
            break


def Broadcast(add, msg, name=""):

    for sockets in clients:
        sockets.send(name.encode("utf-8") + msg)
    x = datetime.datetime.now()
    ed=eid[add]
    val = (msg, ed, "3", "group", x)
    db_insert(val, 1)


server = socket(family=AF_INET, type=SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except OSError:
    print("Server Busy")


serverAudio = socket(family=AF_INET, type=SOCK_STREAM)
try:
    serverAudio.bind((HOSTA, PORTA))
except OSError:
    print("Server Busy")

BufferSize = 1024
serverAudio.listen(2)
print("Waiting for connection audio..")
AcceptThreadAudio = Thread(target=AConnections)
AcceptThreadAudio.start()


server.listen(5)
print("Waiting for Connections... ")
AcceptThread = Thread(target=Connections)
AcceptThread.start()
AcceptThread.join()
server.close()

