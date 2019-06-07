from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("File Transfer")
window.geometry('344x150')

def choose():    
    filename = askopenfilename()
    print(filename)
    
Button1 = Button(window, bg="blue")
Button1.place(relx=0.20, rely=0.3, height=40, width=100)
Button1.configure(text="Choose File", command=choose)

def close():
    window.destroy()

Button2 = Button(window, bg="red")
Button2.place(relx=0.50, rely=0.3, height=40, width=100)
Button2.configure(text="Close", command=close)

window.mainloop()
