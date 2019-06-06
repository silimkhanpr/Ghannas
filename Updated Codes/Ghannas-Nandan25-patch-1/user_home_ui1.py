from tkinter import *
from tkinter import ttk
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import mysql.connector
import tkinter
from mysql.connector import Error
import sys
import os

#database connection
mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="be_project"
    )
cursor=mydb.cursor()

window = Tk()
window.title("User Home")
window.geometry('800x500')

#declaring the message listbox and scrollbar
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
    msg = ChatEntry.get()
    ChatEntry.delete(0, 'end')
    my_msg.set("")  # Clears input field.
    if msg == "quit":
        client_socket.send(msg.encode("utf8"))
        client_socket.close()
        #top.quit()
    else:
        client_socket.send(msg.encode("utf8"))

#eid=sys.argv[1]
eid="3"
query= "select Full_name from employee where Emp_id='"
sql=query+eid+"'"
cursor.execute(sql)
result=cursor.fetchall()
if (result):
 for x in result:
   uname1=x[0] 
sep=' '
uname=uname1.split(sep,1)[0]       

def groupchat():
    os.system('python clientcomb.py')

TButton2 = ttk.Button(window, text="Group chat", command=groupchat)
TButton2.place(relx=0.0, rely=0.0, height=25, width=213)

def notices():
    os.system('python notices_ui.py')

NoticeButton = Button(window, text="Notices", command=notices, bg="red")
NoticeButton.place(relx=0.677, rely=0.0, height=35, width=84)

#left side frame
TFrame1 = ttk.Frame(window)
TFrame1.place(relx=0.0, rely=0.056, relheight=0.955, width=213)

TFrame1.configure(relief='groove')
TFrame1.configure(borderwidth="2")
TFrame1.configure(relief='groove')
TFrame1.configure(width=210)

#search entry box
SearchEntry = ttk.Entry(window)
SearchEntry.place(relx=0.0, rely=0.051, height=22, width=212)

#search button
def search_click(event=None):
    search_res = SearchEntry.get()
    query1 = "SELECT Full_name FROM `employee` WHERE (`Full_name` LIKE '%"+search_res+"%') and (NOT Emp_id="
    sql1=query1+eid+")"
    cursor = mydb.cursor()
    cursor.execute(sql1)
    records = cursor.fetchall()
    if(records):
       for row in records:
            print ("test")
    else:
        print("User not found")
SearchButton = Button(TFrame1, bg="blue")
SearchButton.place(relx=0.0, rely=0.051, height=24, width=85)
SearchButton.configure(text='''Search''', command=search_click)
window.bind("<Return>", search_click)

#all users listed for chats in the form of buttons
query2 = "select Full_name from employee WHERE NOT Emp_id="
sql2=query2+eid
cursor = mydb.cursor()
cursor.execute(sql2)
records = cursor.fetchall()
i = 0
LabelDisp = Label(window, text = "All Contacts:")
LabelDisp.place(relx=0.001, rely=0.177, height=29, width=210)
LabelDisp.config(font=("Times New Roman", 15))

#welcome user label
u="Welcome "+uname
Label1 = Label(window, text = u, fg="red", bg="yellow")
Label1.place(relx=0.432, rely=0.113, height=100, width=300)
Label1.config(font=("Times New Roman", 20))

#what happens when a contact is clicked
def chat_click(st):
    ButtonText = TButton1.cget('text')
    '''query = "select emp_id from employee where full_name='"+ButtonText+"'"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    if(records):
       for row in records:
            receiverid = (row[0])'''
    print("hiii"+st)
    cursor=mydb.cursor()
    query= "SELECT sender_name,message_body FROM group_chat ORDER BY `time` ASC"
    sql=query
    cursor.execute(sql)
    result=cursor.fetchall()
    for x in result:
        print(str(x[0]))
        msg_list.insert(tkinter.END,x[0]+" : "+x[1])

    msg_list.place(relx=0.274, rely=0.210)
 
    ChatEntry.place(relx=0.275, rely=0.925, height=37, width=482)
    ChatEntry.focus()
    SendButton = ttk.Button(window, text="Send", command=send)
    SendButton.place(relx=0.880, rely=0.925, height=37, width=85)
    ChatEntry.bind("<Return>", send)
    
    Label1.destroy()
    LabelUser = Label(window, text=ButtonText, fg="red", bg="yellow")
    LabelUser.place(relx=0.282, rely=0.073, height=60, width=220)
    LabelUser.config(font=("Times New Roman", 20))
    
    videocall = Button (window, text="Video Call")
    videocall.place(relx=0.797, rely=0.1, height=35, width=96)
    audiocall = Button (window, text="Audio Call")
    audiocall.place(relx=0.687, rely=0.1, height=35, width=96)
    filetransfer = Button (window, text="File Transfer")
    filetransfer.place(relx=0.577, rely=0.1, height=35, width=96)

    #when the back button is pressed
    def clearscreen():
        Label1 = Label(window, text = u, fg="red", bg="yellow")
        Label1.place(relx=0.432, rely=0.113, height=100, width=300)
        Label1.config(font=("Times New Roman", 20))
        SendButton.destroy()
        closebutton.destroy()
        videocall.destroy()
        audiocall.destroy()
        filetransfer.destroy()
        ChatEntry.destroy()
        LabelUser.destroy()
        msg_list.destroy()
        scrollbar.destroy()
    
    closebutton = Button(window, text="Back", fg="red", command=clearscreen)
    closebutton.place(relx=0.937, rely=0.1, height=35, width=46)
    
#list of contacts dynamically retrieved from database
for row in records:
    TButton1 = ttk.Button(window)
    TButton1.place(relx=0.001, rely=0.247+i, height=29, width=210)
    TButton1.configure(text=row[0])
    #ButtonText = TButton1.cget('text')
    TButton1.configure(command=chat_click(row[0]))
    i = i + 0.052

cursor.close()
   
def logout():
    window.destroy()

def changepw():
    t="python password_change_ui.py"
    os.system(t+" "+eid)

logoutbutton = Button (window, text="Logout", command=logout, bg="red")
logoutbutton.place(relx=0.907, rely=0.0, height=35, width=86)

changepw = Button (window, text="Change Password", bg="green", command=changepw)
changepw.place(relx=0.777, rely=0.0, height=35, width=106)






'''HOST='172.31.4.90'
PORT = 3000
BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
ReceiveThread = Thread(target=receive).start()
SendThread = Thread(target=send).start()'''

window.mainloop()
