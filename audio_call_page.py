from tkinter import *
from tkinter import ttk
import sys
import os
from DatabaseQuery import db_point
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import pyaudio
from array import array
from test import server_config

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
    socket.close(client)
    

Button1 = Button(master, bg="red")
Button1.place(relx=0.33, rely=0.7, height=40, width=100)
Button1.configure(text="End Call", command=end_call)



HOST = server_config(1)
PORT = 4000
BufferSize = 4096

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024

def SendAudio():
    while True:
        data = stream.read(CHUNK)
        dataChunk = array('h', data)
        vol = max(dataChunk)
        if(vol > 1500):
            print("Recording Sound...")
        else:
            print("Silence..")
        client.sendall(data)


def RecieveAudio():
    while True:
        data = recvall(BufferSize)
        stream.write(data)

def recvall(size):
    databytes = b''
    while len(databytes) != size:
        to_read = size - len(databytes)
        if to_read > (4 * CHUNK):
            databytes += client.recv(4 * CHUNK)
        else:
            databytes += client.recv(to_read)
    return databytes

client = socket(family=AF_INET, type=SOCK_STREAM)
client.connect((HOST, PORT))

audio=pyaudio.PyAudio()
stream=audio.open(format=FORMAT,channels=CHANNELS, rate=RATE, input=True, output = True,frames_per_buffer=CHUNK)


RecieveAudioThread = Thread(target=RecieveAudio).start()
SendAudioThread = Thread(target=SendAudio).start()

master.mainloop()


