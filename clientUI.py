#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import mysql.connector
import os

mydb = mysql.connector.connect(
host="172.26.10.92",
user="root@laptop",
passwd="root",
database="be_project"
)
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            print(msg)
            msg_list.see(tkinter.END)
        except OSError:
            break


def send():  # event is passed by binders.
    msg = entry_field.get()
    entry_field.delete(0, 'end')
    my_msg.set("")  # Clears input field.
    if msg == "quit":
        client_socket.send(msg.encode("utf8"))
        client_socket.close()
        # top.quit()
    else:
        client_socket.send(msg.encode("utf8"))
    print(msg)

top = tkinter.Tk()
top.title("Chat On!")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
cursor=mydb.cursor()
query= "SELECT sender_name,message_body FROM group_chat WHERE group_id = 3"
sql=query
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    msg_list.insert(tkinter.END, x[0]+" : "+x[1])
    print(x[0])

#top.protocol("WM_DELETE_WINDOW", on_closing)

#Socket part
#HOST = input('Enter host: ') # Enter host of the server without inverted commas
HOST= "172.26.10.92"
PORT = 3000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()
tkinter.mainloop()  # for start of GUI  Interface
