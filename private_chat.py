#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import mysql.connector
from test import server_config
import datetime
from mysql.connector import Error
import sys
#import os
#os.system('python serverComb.py')
#db object
mydb = mysql.connector.connect(
     host="192.168.1.35",
     user="root@laptop",
     passwd="root",
     database="be_project"
    )
cursor=mydb.cursor()
#system arguments
#rec_id=sys.argv[1]
#sen_id=sys.argv[2]
rec_id="2"
sen_id="4"
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            #print (msg+"end")
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
#sql_query
query="SELECT sender_name,message_body FROM personal_chat WHERE (`sender_id`='"+sen_id+"' and `receiver_id`='"+rec_id+"') OR (`sender_id`='"+rec_id+"' and `receiver_id`='"+sen_id+"') ORDER BY `time` ASC"
sql=query
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    print(str(x[0]))
    msg_list.insert(tkinter.END,x[0]+" : "+x[1])
        

#Socket part
#HOST = input('Enter host: ') # Enter host of the server without inverted commas
HOST = server_config(1)
PORT = server_config(4)
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()
tkinter.mainloop()  # for start of GUI  Interface
