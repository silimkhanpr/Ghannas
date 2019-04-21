from tkinter import *
from tkinter import ttk
import sys
import os
from DatabaseQuery import db_point
from test import split


eid = sys.argv[1]
# eid = "3"
sql = "select Full_name from employee where Emp_id='"+eid+"'"
result = db_point(sql)
if (result):
    for x in result:
        uname = x[0]
uname = split(uname)
window = Tk()
window.title("User Home")
window.geometry('800x500')


def chat():
    os.system('python clientUI.py')


# chat, group chat button
TButton1 = ttk.Button(window, text="Chat", command=chat)
TButton1.place(relx=0.0, rely=0.0, height=25, width=105)

TButton2 = ttk.Button(window, text="Group chat")
TButton2.place(relx=0.132, rely=0.0, height=25, width=107)


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
    query1 = "SELECT Full_name FROM `employee` WHERE (`Full_name` LIKE '%" + search_res + "%') and (NOT Emp_id='"+eid+"') "
    records = db_point(query1)
    if (records):
        for row in records:
            print(row[0])
    else:
        print("User not found")


SearchButton = Button(TFrame1, bg="blue")
SearchButton.place(relx=0.0, rely=0.051, height=24, width=85)
SearchButton.configure(text='''Search''', command=search_click)
window.bind("<Return>", search_click)

# all users listed for chats in the form of buttons
sql = "select Full_name from employee WHERE NOT Emp_id='"+eid+"'"
records = db_point(sql)
i = 0
LabelDisp = Label(window, text="All Contacts:")
LabelDisp.place(relx=0.001, rely=0.177, height=29, width=210)
LabelDisp.config(font=("Times New Roman", 15))
for row in records:
    TLabel1 = ttk.Label(window)
    TLabel1.place(relx=0.001, rely=0.247 + i, height=29, width=210)
    TLabel1.configure(text=row[0])
    i = i + 0.05


# welcome user label
u = "Welcome " + uname.capitalize()
Label1 = Label(window, text=u, fg="red", bg="yellow")
Label1.place(relx=0.432, rely=0.113, height=100, width=300)
Label1.config(font=("Times New Roman", 20))


def logout():
    window.destroy()


def changepw():
    t = "python password_change_ui.py"
    os.system(t + " " + eid)


logoutbutton = Button(window, text="Logout", command=logout, bg="red")
logoutbutton.place(relx=0.907, rely=0.0, height=35, width=86)

changepw = Button(window, text="Change Password", bg="green", command=changepw)
changepw.place(relx=0.777, rely=0.0, height=35, width=106)

window.mainloop()
