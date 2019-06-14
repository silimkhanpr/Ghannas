import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

window = Tk()
window.title("Server UI")
window.geometry('500x500')

button1 = Button (window, text="Start Server", bg="yellow")
button1.place(relx=0.0, rely=0.0, height=50, width=100)

button2 = Button (window, text="Close Server", bg="yellow")
button2.place(relx=0.0, rely=0.250, height=50, width=100)

button3 = Button (window, text="Refresh Server", bg="yellow")
button3.place(relx=0.0, rely=0.125, height=50, width=100)

Label1 = Label(window, text="Connected to Chat Server : ")
Label1.place(relx=0.35, rely=0.0, height=50, width=250)
Label1.config(font=("Times New Roman", 10))

Label2 = Label(window, text="Connected to Audio Server : ")
Label2.place(relx=0.35, rely=0.35, height=50, width=250)
Label2.config(font=("Times New Roman", 10))

scrollbar = tkinter.Scrollbar()  # To see through previous messages.
chat_list = tkinter.Listbox(height=8, width=45, yscrollcommand=scrollbar.set)
audio_list = tkinter.Listbox(height=8, width=45, yscrollcommand=scrollbar.set)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

chat_list.place(relx=0.35, rely=0.08)
audio_list.place(relx=0.35, rely=0.45)

def close():
    window.destroy()

button4 = Button (window, text="Close", bg="red", command=close)
button4.place(relx=0.0, rely=0.625, height=50, width=100)

window.mainloop()
