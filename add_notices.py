from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

window = Tk()
window.title("Add Notices")
window.geometry('500x250')

label1 = Label(window, text="(Please enter the notice below:)", bg="yellow", fg="black")
label1.place(relx=0.12, rely=0.022, height=49, width=380)
label1.config(font=("Times New Roman", 20))

entry1 = ttk.Entry(window)
entry1.place(relx=0.1, rely=0.284, height=95, width=405)
entry1.focus()

def clicked(event=None):
    label1.configure(text="")
    notice = entry1.get()
    if entry1.get():
        try:
            connection = mysql.connector.connect(host='192.168.43.190',
                                     database='be_project',
                                     user='root@laptop',
                                     password='root')
            query =  "INSERT INTO notices(leader_id, notice_body) VALUES(%s, %s)"
            values = ("2", notice)
            cursor = connection.cursor()
            result  = cursor.execute(query, values)
            connection.commit()
            print ("Record inserted successfully!")
            label1.configure(text="Notice Successfully entered!")
            entry1.delete(0, 'end')
        except mysql.connector.Error as error :
            connection.rollback() #rollback if any exception occured
            print("Failed inserting record into database {}".format(error))
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    else:
        messagebox.showerror('Failure!', 'Enter some text')
        label1.configure(text="(Please enter the notice below:)")
            
def close():
    window.destroy()

button1 = Button (window, text="Submit", command=clicked, bg="blue")
button1.place(relx=0.267, rely=0.733, height=35, width=86)

button2 = Button (window, text="Close", command=close, bg="red")
button2.place(relx=0.507, rely=0.733, height=35, width=86)

window.bind("<Return>", clicked)

window.mainloop()
