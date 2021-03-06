from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import mysql.connector
import datetime
from mysql.connector import Error

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="be_project"
    )
cursor=mydb.cursor()

HOST = "192.168.1.2"
PORT = 3000
uname=""
addresses = {}
clients = {}
eid={}

def Connections():
    while True:
        client, addr = server.accept()
        sep=' '
        addr1=format(addr)
        e=""
        addr2=addr1.split(sep,1)[0]
        addr2=addr2.replace('(','')
        addr2=addr2.replace(',','')
        print(addr2)
        query= "select Emp_id,Full_name from employee where ip_address="+addr2
        cursor.execute(query)
        result=cursor.fetchall()
        if (result):
         for x in result:
           uname1=x[1]
           e=x[0]
        eid[addr2]=e
        sep=' '
        global uname
        uname=uname1.split(sep,1)[0]
        print(uname)
        client.send(("Welcome to Chat Room {}.".format(uname)).encode("utf-8"))
        addresses[client] = addr1
        clients[client] =  uname
        Thread(target = ClientConnection, args=(client, )).start()

def ClientConnection(client):
    query= "SELECT sender_name,message_body FROM personal_chat ORDER BY `time` ASC"
    #WHERE (`sender_id`=2 and `receiver_id`=1) OR (`sender_id`=1 and `receiver_id`=2)
    sql=query
    msg_list=[]
    cursor.execute(sql)
    result=cursor.fetchall()
    for x in result:
        #msg_list.append(x[0]+" : "+x[1])
        print(str(x[0]))
        client.send((x[0]+":"+x[1]+"\n").encode("utf-8"))
    #message = ("{} has joined the chat..").format(uname)
    #Broadcast(message.encode("utf-8"))
    name=clients[client]
    a=addresses[client]
    sep=' '
    addr2=a.split(sep,1)[0]
    addr2=addr2.replace('(','')
    addr2=addr2.replace(',','')

    while True:
        msg = client.recv(BufferSize).decode("utf-8")
        if msg != "quit":
            Broadcast(addr2, msg.encode("utf-8"), name+":")
            print(name+":"+msg)
        else:
            #message = ("{} has left the chat.").format(clients[client])
            #Broadcast(message.encode("utf-8"))
            client.send(("Will see you soon..").encode("utf-8"))
            del clients[client]
            break

def Broadcast(add, msg, name = ""):
    
    for sockets in clients:
        sockets.send(name.encode("utf-8") +msg)
    x = datetime.datetime.now()
    ed=eid[add]
    sql="insert into message (message_body,sender_id,receiver_id,message_type,time) values (%s,%s,%s,%s,%s)"
    val=(msg,ed,"2","personal",x)
    cursor.execute(sql,val)
    mydb.commit()

#a=eval(input('Enter 1 to start chat server'))
a=1
if a==1:
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
