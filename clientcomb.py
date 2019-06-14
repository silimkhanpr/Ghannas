#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from test import server_config
from DatabaseQuery import message_populate


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            # print (msg+"end")
            msg_list.see(tkinter.END)
        except OSError:
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    if msg == "quit":
        client_socket.send(msg.encode("utf8"))
        client_socket.close()
        # top.quit()
    else:
        client_socket.send(msg.encode("utf8"))


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
t = 3
a, i = message_populate(str(t))                      # code to populate previous messages
j = 0
while j < i:
    msg_list.insert(tkinter.END, a[j])
    j += 1


# Socket part
HOST, PORT = server_config()
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()
tkinter.mainloop()  # for start of GUI  Interface
