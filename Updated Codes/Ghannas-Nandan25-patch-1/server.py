from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = "172.31.4.71"
PORT = 3000
PORT1=4000

addresses = {}
clients = {}
BufferSize = 1024



def Connections1():
    while True:
        client, addr = serverAudio.accept()
        print("{} is connected!!".format(addr))
        client.send(("Welcome to Chat Room. Type {quit} to exit. Enter your name: ").encode("utf-8"))
        addresses[client] = addr
        Thread(target = ClientConnection, args=(client, )).start()



def Connections():
    while True:
        client, addr = serverVideo.accept()
        print("{} is connected!!".format(addr))
        client.send(("Welcome to Chat Room. Type {quit} to exit. Enter your name: ").encode("utf-8"))
        addresses[client] = addr
        Thread(target = ClientConnection, args=(client, )).start()

def ClientConnection(client):
    name = client.recv(BufferSize).decode("utf-8")
    client.send(("Hello {}".format(name)).encode("utf-8"))
    message = ("{} has joined the chat..").format(name)
    Broadcast(message.encode("utf-8"))
    clients[client] = name
    while True:
        msg = client.recv(BufferSize).decode("utf-8")
        if msg != "quit":
            print(msg)
            Broadcast(msg.encode("utf-8"), name + ": ")
        else:
            message = ("{} has left the chat.").format(clients[client])
            Broadcast(message.encode("utf-8"))
            client.send(("Will see you soon..").encode("utf-8"))
            del clients[client]
            break

def Broadcast(msg, name = ""):
    for sockets in clients:
        sockets.send(name.encode("utf-8") + msg)





serverVideo = socket(family=AF_INET, type=SOCK_STREAM)
try:
    serverVideo.bind((HOST, PORT))
except OSError:
    print("Server Busy"+str(PORT))

serverAudio = socket(family=AF_INET, type=SOCK_STREAM)
try:
    serverAudio.bind((HOST, PORT1))
except OSError:
    print("Server1 Busy"+str(PORT1))
    



    
serverAudio.listen(2)
print("Waiting for User")
AcceptThreadAudio = Thread(target=Connections1)
AcceptThreadAudio.start()

serverVideo.listen(2)
print("Waiting for connection User 1")
AcceptThreadVideo = Thread(target=Connections)
AcceptThreadVideo.start()
AcceptThreadVideo.join()
serverVideo.close()
