from tkinter import *
from tkinter import ttk
import sys
import hashlib
import mysql.connector
window = Tk()
window.title("Change password")
window.geometry('350x350')

t=sys.argv[1]


from mysql.connector import Error
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="be_project"
)
cursor=mydb.cursor()
query= "select password from users where Emp_id='"
sql=query+t+"'"
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    pass1=x[0]

     

label1 = Label(window, text="Current*:", fg="red")
label1.place(relx=0.25, rely=0.15, height=25, width=76)

label2 = Label(window, text="New*:", fg="red")
label2.place(relx=0.25, rely=0.25, height=25, width=76)

label3 = Label(window, text="(Change your password here:)", fg="blue")
label3.place(relx=0.12, rely=0.0, height=35, width=150)

entry1 = ttk.Entry(window,show="*")
entry1.place(relx=0.45, rely=0.15, height=25, width=125)

entry2 = ttk.Entry(window,show="*")
entry2.place(relx=0.45, rely=0.25, height=25, width=125)

def clicked(event=None):
    print ("test!")
    p=entry1.get()
    p1=entry2.get()
    m2 = hashlib.md5()
    m2.update(p1.encode('utf-8'))
    new_pass=m2.hexdigest()   #new password
    m = hashlib.md5()
    m.update(p.encode('utf-8'))
    pass2=m.hexdigest()   #original password
    #sql code 
    if pass2==pass1:
        print(new_pass)
        query =  "UPDATE users SET password ='" 
        sql=query+new_pass+"'WHERE Emp_iD ="+t;
        values = (new_pass)
        result2  = cursor.execute(sql, values)
        mydb.commit()
        print ("Record inserted successfully!")
    else:
       print("password doesnt match original password")
    

button1 = Button(window, text="Submit", command=clicked, bg="blue")
button1.place(relx=0.38, rely=0.35, height=30, width=75)


def close():
    window.destroy()
    
button2 = Button (window, text="Close", command=close, bg="red")
button2.place(relx=0.68, rely=0.35, height=30, width=75)

window.bind("<Return>", clicked)

window.mainloop()
