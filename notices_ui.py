import tkinter
from tkinter import ttk
from tkinter import *
from DatabaseQuery import db_point

window = Tk()
window.title("Notices")

notice_frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(notice_frame)      # displays all notices
# this will contain the messages.
notice_list = tkinter.Listbox(notice_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
notice_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
notice_list.pack()
notice_frame.pack()


def close():
    window.destroy()


button1 = Button (window, text="Close", command=close, bg="red")
button1.place(relx=0.862, rely=0.930, height=35, width=86)

SearchEntry = ttk.Entry(window)
SearchEntry.place(relx=0.0, rely=0.930, height=35, width=412)
SearchEntry.focus()


def search_click(event=None):
    search = SearchEntry.get()
    query1 = "SELECT notice_body,date_created FROM `notices` WHERE (`notice_body` LIKE '%" + search + "%') ORDER " \
               "BY `date_created` ASC "
    records = db_point(query1)
    if records:
      for row in records:
        print(row[0]+":\t"+str(x[1]))
    else:
        print("Notice not found")


SearchButton = Button(window, bg="blue")
SearchButton.place(relx=0.662, rely=0.930, height=35, width=86)
SearchButton.configure(text="Search", command=search_click)
window.bind("<Return>", search_click)
query1 = "SELECT notice_body,date_created FROM `notices`ORDER BY `date_created` ASC "
result = db_point(query1)
for x in result:
    notice_list.insert(tkinter.END, x[0]+":\t"+str(x[1]))
    print(x[0]+":\t"+str(x[1]))

window.mainloop()
