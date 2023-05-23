from tkinter import *
from datetime import datetime

# Init root window, frames, labels
root = Tk()
root.title("Digital Clock")
frm = Frame(root)
label_time = Label(frm, text="", padx=300, pady=100, bg="black", fg="cyan", font=("Arial", 30, "bold"), relief="flat")

# Function for updating clock value
def update_clk():
    cur_time = datetime.now().strftime("%H:%M:%S")
    label_time.configure(text=cur_time)
    label_time.after(80, update_clk)
    label_time.grid()

# Pack and ship
frm.pack()
label_time.pack()
update_clk()
root.mainloop()