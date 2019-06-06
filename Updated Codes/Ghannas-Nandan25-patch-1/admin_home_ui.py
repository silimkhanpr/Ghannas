from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os
import sys
mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="be_project"
    )
cursor=mydb.cursor()
eid=sys.argv[1]
#eid="2"
query= "select Full_name from employee where Emp_id='"
sql=query+eid+"'"
cursor.execute(sql)
result=cursor.fetchall()
if (result):
 for x in result:
   uname1=x[0] 
sep=' '
uname=uname1.split(sep,1)[0] 

window = Tk()
window.title("Admin Home")
window.geometry('800x500')

#establish connection
connection = mysql.connector.connect(host='localhost',
                            database='be_project',
                            user='root',
                            password='')

#chat, video call, group chat, notices button
TButton1 = ttk.Button(window, text="Chats")
TButton1.place(relx=0.0, rely=0.0, height=25, width=40)

TButton2 = ttk.Button(window, text="Video call")
TButton2.place(relx=0.049, rely=0.0, height=25, width=40)

TButton2 = ttk.Button(window, text="Video call")
TButton2.place(relx=0.049, rely=0.0, height=25, width=60)

TButton3 = ttk.Button(window, text="Group chat")
TButton3.place(relx=0.122, rely=0.0, height=25, width=70)

TButton4 = ttk.Button(window, text="Notices")
TButton4.place(relx=0.209, rely=0.0, height=25, width=49)

#left side frame
TFrame1 = ttk.Frame(window)
TFrame1.place(relx=0.0, rely=0.055, relheight=0.955, width=212)

TFrame1.configure(relief='groove')
TFrame1.configure(borderwidth="2")
TFrame1.configure(relief='groove')
TFrame1.configure(width=210)

#search entry box
SearchEntry = ttk.Entry(window)
SearchEntry.place(relx=0.0, rely=0.051, height=22, width=210)

#search button
def search_click(event=None):
    search_res = SearchEntry.get()
    query1 = "SELECT Full_name FROM `employee` WHERE (`Full_name` LIKE '%"+search_res+"%') and (NOT Emp_id="
    sql1=query1+eid+")"
    cursor = connection.cursor()
    cursor.execute(sql1)
    records = cursor.fetchall()
    if(records): 
       for row in records:
          print (row[0])
    else :
        print("Not found")
window.bind("<Return>", search_click)

SearchButton = Button(TFrame1, bg="blue")
SearchButton.place(relx=0.0, rely=0.051, height=24, width=85)
SearchButton.configure(text='''Search''', command=search_click)
#separators
TSeparator1 = ttk.Separator(TFrame1)
TSeparator1.place(relx=0.50, rely=0.153, width=210)

#all users listed for chats in the form of buttons
query2 = "select Full_name from employee WHERE NOT Emp_id="
sql2=query2+eid
cursor = connection.cursor()
cursor.execute(sql2)
records = cursor.fetchall()
i = 0
for row in records:
    TButton3 = ttk.Button(TFrame1)
    TButton3.place(relx=0.0, rely=0.147+i, height=29, width=210)
    TButton3.configure(text=row[0])
    i = i + 0.1
cursor.close()
   
#welcome user label
u="Welcome "+uname
Label1 = Label(window, text = u, fg="red")
Label1.place(relx=0.432, rely=0.113, height=100, width=300)
Label1.config(font=("Times New Roman", 30))

def logout():
    window.destroy()

logoutbutton = Button (window, text="Logout", command=logout, bg="red")
logoutbutton.place(relx=0.907, rely=0.0, height=35, width=86)

def redirect():
    os.system('python registration_page_ui.py')

ANUButton = Button(window, bg="yellow", fg="green", text="Add New Users!", command=redirect)
ANUButton.place(relx=0.532, rely=0.542, height=70, width=120)

window.mainloop()
