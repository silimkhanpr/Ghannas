
from threading import Thread
import datetime
from DatabaseQuery import *
from socket import AF_INET, SOCK_STREAM, socket
from test import server_config,split

HOST, PORT = server_config()
uname = ""
addresses = {}
clients = {}
eid = {}


def Connections():
    while True:
        client, addr = server.accept()
        addr1 = format(addr)
        addr2 = split(addr,2)
        print(addr2)
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
BufferSize = 1024
server.listen(5)
print("Waiting for Connections... ")
AcceptThread = Thread(target=Connections)
AcceptThread.start()
AcceptThread.join()
server.close()