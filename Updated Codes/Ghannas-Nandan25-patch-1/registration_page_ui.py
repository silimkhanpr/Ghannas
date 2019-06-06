from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

master = Tk()
master.geometry("800x500")
master.title("Registration")

label1 = Label(master, text="Full Name:", fg="red")
label1.place(relx=0.183, rely=0.244, height=29, width=106)

label2 = Label(master, text="Designation:", fg="red")
label2.place(relx=0.183, rely=0.311, height=29, width=106)

label3 = Label(master, text="Email-id:", fg="red")
label3.place(relx=0.183, rely=0.378, height=29, width=106)

label4 = Label(master, text="DOB (YY-MM-DD):", fg="red")
label4.place(relx=0.183, rely=0.444, height=29, width=106)

label5 = Label(master, text="(Please enter the details below:)", bg="yellow", fg="black")
label5.place(relx=0.05, rely=0.022, height=49, width=380)
label5.config(font=("Times New Roman", 20))

label6 = Label(master, fg="green")
label6.place(relx=0.267, rely=0.633, height=35, width=136)

entry1 = ttk.Entry(master)
entry1.place(relx=0.367, rely=0.244, relheight=0.069, relwidth=0.343)

entry2 = ttk.Entry(master)
entry2.place(relx=0.367, rely=0.311, relheight=0.069, relwidth=0.343)

entry3 = ttk.Entry(master)
entry3.place(relx=0.367, rely=0.378, relheight=0.069, relwidth=0.343)

entry4 = ttk.Entry(master)
entry4.place(relx=0.367, rely=0.444, relheight=0.069, relwidth=0.343)

TSeparator1 = ttk.Separator(master)
TSeparator1.place(relx=0.167, rely=0.244, relheight=0.267)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(master)
TSeparator2.place(relx=0.167, rely=0.244, relwidth=0.533)

TSeparator3 = ttk.Separator(master)
TSeparator3.place(relx=0.167, rely=0.511, relwidth=0.533)

TSeparator4 = ttk.Separator(master)
TSeparator4.place(relx=0.367, rely=0.244, relheight=0.267)
TSeparator4.configure(orient="vertical")

def clicked():
    fullname = entry1.get()
    designation = entry2.get()
    emailid = entry3.get()
    dob = entry4.get()
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='be_project',
                                 user='root',
                                 password='')
        query =  "INSERT INTO employee(Full_name, Designation, Email_id, Dob) VALUES(%s, %s, %s, %s)"
        values = (fullname, designation, emailid, dob)
        cursor = connection.cursor()
        result  = cursor.execute(query, values)
        connection.commit()
        print ("Record inserted successfully!")
        label6.configure(text="Registration Success!")
    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into database {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

button1 = Button (master, text="submit", command=clicked, bg="blue")
button1.place(relx=0.267, rely=0.533, height=35, width=136)


mainloop( )
