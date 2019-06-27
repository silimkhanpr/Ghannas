from tkinter import *
import tkinter as tk
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
       
Label1 = Label(master, text="Pranav Silimkhan")
Label1.place(relx=0.25, rely=0.45, height=100, width=180)
Label1.config(font=("Times New Roman", 15))

def update_timeText():
    if (state):
        global timer
        timer[2] += 1
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        timeString = pattern.format(timer[0], timer[1], timer[2])
        timeText.configure(text=timeString)
    master.after(10, update_timeText)

state = True
timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}'
timeText = tk.Label(master, text="00:00", font=("Helvetica", 15))
timeText.place(relx=0.40, rely=0.68)
update_timeText()

canvas = Canvas(master, width = 150, height = 150)      
canvas.pack()      
img = PhotoImage(file="icon.ppm")
canvas.create_image(20,40, anchor=NW, image=img)        

def end_call():
    master.destroy()
    socket.close(client)
    
Button1 = Button(master, bg="red")
Button1.place(relx=0.33, rely=0.8, height=40, width=100)
Button1.configure(text="End Call", command=end_call)

HOST = server_config(1)
PORT = server_config(3)
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


