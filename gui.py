from tkinter import *
from tkinter import ttk
from datetime import datetime

root = Tk()

frm = Frame(root).grid()

cur_time = datetime.now().strftime("%H:%M:%S")
label_time = Label(frm, text=cur_time, padx=300, pady=100).grid()

while True:
    cur_time = datetime.now().strftime("%H:%M:%S")

    root.update()



root.mainloop()