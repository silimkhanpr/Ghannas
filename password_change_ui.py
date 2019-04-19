from tkinter import *
from tkinter import ttk
import sys
from test import encrypt_code
from DatabaseQuery import get_password,password_reset
window = Tk()
window.title("Change password")
window.geometry('350x350')

# t = sys.argv[1]
t="3"
pass1 = get_password(t)

label1 = Label(window, text="Current*:", fg="red")
label1.place(relx=0.25, rely=0.15, height=25, width=76)

label2 = Label(window, text="New*:", fg="red")
label2.place(relx=0.25, rely=0.25, height=25, width=76)

label3 = Label(window, text="(Change your password here:)", fg="blue")
label3.place(relx=0.12, rely=0.0, height=35, width=150)

entry1 = ttk.Entry(window, show="*")
entry1.place(relx=0.45, rely=0.15, height=25, width=125)

entry2 = ttk.Entry(window, show="*")
entry2.place(relx=0.45, rely=0.25, height=25, width=125)


def clicked(event=None):
    p = entry1.get()
    p1 = entry2.get()
    new_pass = encrypt_code(p1)  # new password
    pass2 = encrypt_code(p)  # original password
    # sql code
    if pass2 == pass1:  # check if original password match with password from db
        print(new_pass)
        password_reset(new_pass, t)
        print("Record inserted successfully!")
    else:
        print("password doesnt match original password")


button1 = Button(window, text="Submit", command=clicked, bg="blue")
button1.place(relx=0.38, rely=0.35, height=30, width=75)


def close():
    window.destroy()


button2 = Button(window, text="Close", command=close, bg="red")
button2.place(relx=0.68, rely=0.35, height=30, width=75)

window.bind("<Return>", clicked)

window.mainloop()
