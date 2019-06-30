from threading import Thread
import datetime
from DatabaseQuery import *
from socket import AF_INET, SOCK_STREAM, socket
from test import server_config, split


HOST = server_config(1)
PORT = server_config(4)
uname = ""
addresses = {}
clients = {}
eid = {}
rec_Id = ""
HOSTA = server_config(1)
PORTA = server_config(3)
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
        addr1 = split(addr1, 2)
        print(addr1)
        global uname
        uname, eid[addr1] = emp_ip(addr1)
        uname = uname.capitalize()
        print(uname)
        addresses[client] = addr1
        clients[client] = uname
        Thread(target=ClientConnection, args=(client, )).start()

def ClientConnection(client):
    name = clients[client]
    a = addresses[client]
    addr2 = split(a, 2)
    global rec_Id
    rec_Id = client.recv(BufferSize).decode("utf-8")
    #print("receiver id is " + rec_Id)

    while True:
        ms = client.recv(BufferSize).decode("utf-8")
        msg = ms.split(", ", 1)

        rec_Id = msg[0]
        if msg[1] != "quit":
            Broadcast(addr2, msg[1].encode("utf-8"), name+":")
            print(name+":"+msg[1])
        else:
            client.send(("Will see you soon..").encode("utf-8"))
            del clients[client]
            break


def Broadcast(add, msg, name=""):
    for sockets in clients:
        receiver_ip = emp_ip(rec_Id, 1)
        print(receiver_ip)
        soc = str(sockets).split("=('", 1)
        s = soc[1].split("',", 1)
        print("broadcast receiver"+s[1])
        ed = eid[add]
        x = datetime.datetime.now()
        if receiver_ip == receiver_ip:
            val = (msg, ed, int(rec_Id), None, "private", x)
            print(val)
            db_insert(val, 1)
        else:
            val = (msg, ed, None, "3", "group", x)
            print(val)
            db_insert(val, 1)

    sockets.send(name.encode("utf-8") + msg)
    print(rec_Id)
    # val = (msg, ed, int(rec_Id), "private", x)
    # db_insert(val, 1)


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
