from tkinter import *
from tkinter import ttk
import sys
import os
from DatabaseQuery import db_point

master = Tk()
master.geometry("300x300")

temp = sys.argv[1]

master.title("Audio Call")
query2 = "select Full_name from employee WHERE Emp_id='"+temp+"'"
records = db_point(query2)
if records:
    for x in records:
        name = x[0]
       
Label1 = Label(master, text=name)
Label1.place(relx=0.25, rely=0.45, height=100, width=180)
Label1.config(font=("Times New Roman", 15))
 
canvas = Canvas(master, width = 150, height = 150)      
canvas.pack()      
img = PhotoImage(file="icon.ppm")
canvas.create_image(20,40, anchor=NW, image=img)        

def end_call():
    master.destroy()

Button1 = Button(master, bg="red")
Button1.place(relx=0.33, rely=0.7, height=40, width=100)
Button1.configure(text="End Call", command=end_call)

master.mainloop()

