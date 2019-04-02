import tkinter
from tkinter import ttk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="be_project"
)

window = Tk()
window.title("Notices")

notice_frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(notice_frame) #displays all notices
# this will contain the messages.
notice_list = tkinter.Listbox(notice_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
notice_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
notice_list.pack()
notice_frame.pack()

def close():
    window.destroy()

button1 = Button (window, text="Close", command=close, bg="red")
button1.place(relx=0.862, rely=0.930, height=35, width=86)

SearchEntry = ttk.Entry(window)
SearchEntry.place(relx=0.0, rely=0.930, height=35, width=412)
SearchEntry.focus()

def search_click(event=None):
    search=SearchEntry.get()
    query1 = "SELECT notice_body FROM `notices` WHERE (`notice_body` LIKE '%"+search+"%')"
    cursor = mydb.cursor()
    cursor.execute(query1)
    records = cursor.fetchall()
    if(records):
       for row in records:
            print (row[0])
    else:
        print("Notice not found")

SearchButton = Button(window, bg="blue")
SearchButton.place(relx=0.662, rely=0.930, height=35, width=86)
SearchButton.configure(text="Search", command=search_click)
window.bind("<Return>", search_click)

cursor=mydb.cursor()
query= "SELECT notice_body FROM notices"
sql=query
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    notice_list.insert(tkinter.END, x[0])
    print(x[0])

window.mainloop()
