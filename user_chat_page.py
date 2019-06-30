from importlib import reload
from tkinter import *
from tkinter import ttk
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from test import split, server_config
from DatabaseQuery import db_point, message_populate
import tkinter
import os

eid = sys.argv[1]
receiver_Id = ""
eid = str(eid)
window = Tk()
window.title("User Home")
window.geometry('800x500')

# declaring the message listbox and scrollbar
scrollbar = tkinter.Scrollbar()  # To see through previous messages.
msg_list = tkinter.Listbox(height=22, width=94, yscrollcommand=scrollbar.set)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

ChatEntry = ttk.Entry(window)


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


def send(event=None):  # event is passed by binders.
    # client_socket.send(eid.encode("utf8"))
    # client_socket.send(str(receiverid).encode("utf8"))
    ms = ChatEntry.get()
    msg = str(receiver_Id) + ", " + ms
    ChatEntry.delete(0, 'end')
    my_msg.set("")  # Clears input field.
    if msg == "quit":
        client_socket.send(msg.encode("utf8"))
        client_socket.close()
        # top.quit()
    else:
        client_socket.send(msg.encode("utf8"))


query = "select Full_name from employee where Emp_id='" + eid + "'"
result = db_point(query)
if result:
    for x in result:
        uname1 = x[0]

uname = split(uname1)
uname = uname.capitalize()


def groupchat():
    flag = 1
    #os.system('python clientcomb.py')


TButton2 = ttk.Button(window, text="Group chat", command=groupchat)
TButton2.place(relx=0.0, rely=0.0, height=25, width=213)


def notices():
    os.system('python notices_ui.py')


NoticeButton = Button(window, text="Notices", command=notices, bg="red")
NoticeButton.place(relx=0.677, rely=0.0, height=35, width=84)

# left side frame
TFrame1 = ttk.Frame(window)
TFrame1.place(relx=0.0, rely=0.056, relheight=0.955, width=213)
TFrame1.configure(relief='groove')
TFrame1.configure(borderwidth="2")
TFrame1.configure(relief='groove')
TFrame1.configure(width=210)

# search entry box
SearchEntry = ttk.Entry(window)
SearchEntry.place(relx=0.0, rely=0.051, height=22, width=212)


# search button
def search_click(event=None):
    search_res = SearchEntry.get()
    query1 = "SELECT Full_name FROM `employee` WHERE (`Full_name` LIKE '%" + search_res + "%') and (NOT Emp_id='" + eid + "')"
    records = db_point(query1)
    if records:
        for row in records:
            print(row[0])
    else:
        print("User not found")


SearchButton = Button(TFrame1, bg="blue")
SearchButton.place(relx=0.0, rely=0.051, height=24, width=85)
SearchButton.configure(text='''Search''', command=search_click)
window.bind("<Return>", search_click)

# all users listed for chats in the form of buttons
query2 = "select Emp_id, Full_name from employee WHERE NOT Emp_id='"+eid+"'"
records = db_point(query2)
n = 0
LabelDisp = Label(window, text="All Contacts:")
LabelDisp.place(relx=0.001, rely=0.177, height=29, width=210)
LabelDisp.config(font=("Times New Roman", 15))

# welcome user label
u = "Welcome " + uname
Label1 = Label(window, text=u, fg="red", bg="yellow")
Label1.place(relx=0.432, rely=0.113, height=100, width=300)
Label1.config(font=("Times New Roman", 20))


# code when a contact is clicked
def chat_click(receiverid, fullname):


    global receiver_Id
    receiver_Id = receiverid



    print("sender id is " + eid)
    print("receiver id is " + str(receiverid))
    msg_list.delete(0, tkinter.END)
    # ContactButton.config(state="disabled")

    a, i = message_populate(eid, str(receiverid))  # code to populate previous messages
    j = 0
    while j < i:
        msg_list.insert(tkinter.END, a[j])
        j += 1

    msg_list.place(relx=0.274, rely=0.210)
    ChatEntry.place(relx=0.275, rely=0.925, height=37, width=482)
    ChatEntry.focus()
    SendButton = ttk.Button(window, text="Send", command=send)
    SendButton.place(relx=0.880, rely=0.924, height=39, width=85)
    ChatEntry.bind("<Return>", send)

    Label1.destroy()
    LabelUser = Label(window, text=fullname, fg="red", bg="yellow")
    LabelUser.place(relx=0.282, rely=0.073, height=60, width=220)
    LabelUser.config(font=("Times New Roman", 20))

    videocall = Button(window, text="Video Call")
    videocall.place(relx=0.797, rely=0.1, height=35, width=96)
    audiocall = Button(window, text="Audio Call")
    audiocall.place(relx=0.687, rely=0.1, height=35, width=96)
    filetransfer = Button(window, text="File Transfer")
    filetransfer.place(relx=0.577, rely=0.1, height=35, width=96)

# list of contacts dynamically retrieved from database


if records:
    for row in records:
        ContactButton = ttk.Button(window)
        ContactButton.config(text="%s" % row[1],
                             command=lambda receiverid=row[0], fullname=row[1]: chat_click(receiverid, fullname))
        ContactButton.place(relx=0.001, rely=0.247 + n, height=29, width=210)
        n = n + 0.052


def logout():
    window.destroy()
    socket.close(client_socket)


def changepw():
    t = "python password_change_ui.py"
    os.system(t + " " + eid)


logoutbutton = Button(window, text="Logout", command=logout, bg="red")
logoutbutton.place(relx=0.907, rely=0.0, height=35, width=86)

changepw = Button(window, text="Change Password", bg="green", command=changepw)
changepw.place(relx=0.777, rely=0.0, height=35, width=106)

HOST = server_config(1)
PORT = server_config(4)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()

window.mainloop()