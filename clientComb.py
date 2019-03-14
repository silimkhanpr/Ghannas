from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import tkinter as tk


#HOST = input("Enter Host IP: ")
HOST = "172.31.4.70"
#PORT = eval(input("Enter Port No: "))
PORT = 2000
BufferSize = 1024


def Recieve():
    while True:
        try:
            msg = client.recv(BufferSize).decode("utf-8")
            print(msg)
            w = tk.Label(root, text=msg)
            w.pack()
        except OSError:
            break

def Send():
    while True:
        msg = input()
        if msg == "quit":
            client.send(msg.encode("utf-8"))
            client.close()
            break
        else:
            client.send(msg.encode("utf-8"))


a=eval(input(' Press 1 to chat via text '))
root = tk.Tk()

if a==1:
    
    print(a)
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect((HOST, PORT))
    RecieveThread = Thread(target=Recieve).start()
    SendThread = Thread(target=Send).start()
  #  name = StringVar()
    #entry_box = Entry(root, textvariable=name, width=50, bg="white").place(x=200,y=210)
root.mainloop()
