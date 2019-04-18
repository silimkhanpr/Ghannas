from tkinter import *
from tkinter import ttk
from DatabaseQuery import db_insert
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

label5 = Label(master, text="IP Address:", fg="red")
label5.place(relx=0.183, rely=0.510, height=29, width=106)

label6 = Label(master, text="(Please enter the details below:)", bg="yellow", fg="black")
label6.place(relx=0.05, rely=0.022, height=49, width=380)
label6.config(font=("Times New Roman", 20))

label7 = Label(master, fg="green")
label7.place(relx=0.267, rely=0.633, height=35, width=136)

entry1 = ttk.Entry(master)
entry1.place(relx=0.367, rely=0.244, relheight=0.069, relwidth=0.343)
entry1.focus()

entry2 = ttk.Entry(master)
entry2.place(relx=0.367, rely=0.311, relheight=0.069, relwidth=0.343)

entry3 = ttk.Entry(master)
entry3.place(relx=0.367, rely=0.378, relheight=0.069, relwidth=0.343)

entry4 = ttk.Entry(master)
entry4.place(relx=0.367, rely=0.444, relheight=0.069, relwidth=0.343)

entry5 = ttk.Entry(master)
entry5.place(relx=0.367, rely=0.510, relheight=0.069, relwidth=0.343)

TSeparator1 = ttk.Separator(master)
TSeparator1.place(relx=0.167, rely=0.244, relheight=0.337)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(master)
TSeparator2.place(relx=0.167, rely=0.244, relwidth=0.533)

TSeparator3 = ttk.Separator(master)
TSeparator3.place(relx=0.167, rely=0.578, relwidth=0.533)

TSeparator4 = ttk.Separator(master)
TSeparator4.place(relx=0.367, rely=0.244, relheight=0.267)
TSeparator4.configure(orient="vertical")

def clicked(event=None):
    label6.configure(text="")
    fullname = entry1.get()
    designation = entry2.get()
    emailid = entry3.get()
    dob = entry4.get()
    ip=entry5.get()
    if entry1.get()and entry2.get()and entry3.get()and entry4.get() and entry5.get():

            values = (fullname, designation, emailid, dob,ip)
            db_insert(values,2)
            print ("Record inserted successfully!")
            label6.configure(text="Registration Success!")
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
def close():
    master.destroy()

button1 = Button (master, text="Submit", command=clicked, bg="blue")
button1.place(relx=0.267, rely=0.633, height=35, width=136)

button2 = Button (master, text="Close", command=close, bg="red")
button2.place(relx=0.507, rely=0.633, height=35, width=86)

master.bind("<Return>", clicked)

mainloop( )
