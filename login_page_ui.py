from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import hashlib
from DatabaseQuery import user_login
import os

master =Tk()
master.geometry("350x350")
master.title("Login")

label1 = Label(master, text="Username:", fg="red")
label1.place(relx=0.25, rely=0.15, height=25, width=76)

label2 = Label(master, text="Password:", fg="red")
label2.place(relx=0.25, rely=0.25, height=25, width=76)

label3 = Label(master, text="(Please fill the details below:)", fg="blue")
label3.place(relx=0.12, rely=0.0, height=35, width=150)

entry1 = ttk.Entry(master)
entry1.place(relx=0.45, rely=0.15, height=25, width=125)

entry2 = ttk.Entry(master,show="*")
entry2.place(relx=0.45, rely=0.25, height=25, width=125)

label4 = Label(master, fg="green")
label4.place(relx=0.35, rely=0.45, height=30, width=120)

def clicked(event=None):
    username = entry1.get()
    password = entry2.get()
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    pass1=m.hexdigest()
    uname=str(username)
    result=user_login(uname)
    if (result):
         for x in result:
             pass2=x[2]
             utype=x[3]
             eid=x[0]
             if (pass1==pass2):
                 if utype=="standard":
                    print(uname+" Logged in as standard user")
                    label4.configure(text="Login Success!")
                    user="python C:\\Users\\nanda\\Desktop\\project\\user_home_ui.py"
                    #print (user+" "+str(eid))
                    os.system(user+" "+str(eid))
                 elif utype=="admin":
                    print(uname+" Logged in as admin")
                    user="python admin_home_ui.py"
                    os.system(user+" "+str(eid))
                    label4.configure(text="Login Success!")
             else:
                 messagebox.showerror('Login Failure', 'Invalid Password')

    else:
          messagebox.showerror('Login Failure', 'Invalid Username')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

button1 = Button(master, text="Login", command=clicked, bg="blue")
button1.place(relx=0.48, rely=0.35, height=30, width=100)

master.bind("<Return>", clicked)

mainloop( )


