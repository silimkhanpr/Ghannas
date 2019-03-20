from socket import AF_INET, SOCK_STREAM, socket
from tkinter import *
from tkinter import ttk
from threading import Thread
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="be_project"
)
master =Tk()
master.geometry("350x350")
master.resizable(0, 0)

entry1 = ttk.Entry(master)

entry1.grid(row=5, column=9)



mycursor=mydb.cursor()
#HOST = input("Enter Host IP: ")
HOST = "192.168.1.36"
#PORT = eval(input("Enter Port No: "))
PORT = 3000
BufferSize = 1024

def Send():
    while True:
        msg = input()
        if msg == "quit":
            client.send(msg.encode("utf-8"))
            client.close()
            break
        else:
            client.send(msg.encode("utf-8"))
            #sql="insert into message (message_body,message_type) values (%s,%s)"
            #val=(msg,"personal")
            #mycursor.execute(sql,val)
            #mydb.commit()
               
            
            
def Send_chat():
    
        msg ="t"
        temp=entry1.get()
        print(temp)
        if msg == "quit":
            client.send(msg.encode("utf-8"))
            client.close()
           
        else:
            client.send(msg.encode("utf-8"))
            #sql="insert into message (message_body,message_type) values (%s,%s)"
            #val=(msg,"personal")
            #mycursor.execute(sql,val)
            #mydb.commit()
            
            


#a=eval(input(' Press 1 to chat via text '))
#root = tk.Tk()
a=1

if a==1:
    
    print(a)
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect((HOST, PORT))
    #RecieveThread = Thread(target=Recieve).start()
    SendThread = Thread(target=Send).start()

w = ttk.Button (master, text="Login", command=Send_chat)
w.grid(row=20, column=5)
mainloop( )
