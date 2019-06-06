#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import mysql.connector
#import sys
#import os
#os.system('python serverComb.py')
"""host="localhost",
user="root",
passwd="",
database="be_project"
)"""
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            msg_list.see(tkinter.END)
        except OSError:
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    if msg == "quit":
        client_socket.send(msg.encode("utf8"))
        client_socket.close()
        #top.quit()
    else:
        client_socket.send(msg.encode("utf8"))

#def on_closing(event=None):
 #   """This function is to be called when the window is closed."""
  #  my_msg.set("{quit}")
   # send()

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
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
#cursor=mydb.cursor()
#query= "SELECT sender_name,message_body FROM personal_chat WHERE (`sender_id`=2 and `receiver_id`=1) OR (`sender_id`=1 and `receiver_id`=2)"
#sql=query
#cursor.execute(sql)
#result=cursor.fetchall()
#for x in result:
    #msg_list.insert(tkinter.END, x[0]+" : "+x[1])
    #print(x[0])

#top.protocol("WM_DELETE_WINDOW", on_closing)

#Socket part
#HOST = input('Enter host: ') # Enter host of the server without inverted commas
HOST='172.31.4.90'
PORT = 3000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()
tkinter.mainloop()  # for start of GUI  Interface
