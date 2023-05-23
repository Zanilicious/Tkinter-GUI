from tkinter import Tk, Frame, Button, Label
# from math import *

# Define sizes
UNIT_HEIGHT = 100
UNIT_WIDTH = 100

# Create root window, add frames
root_window = Tk()
root_window.title("Calculator")
inp_frm = Frame(root_window, height=UNIT_HEIGHT, width=UNIT_WIDTH*4, padx=10, pady=10, background="white")
btn_frm = Frame(root_window, height=UNIT_WIDTH*5, width=UNIT_WIDTH*4, padx=10, pady=10)

# Define buttons
btn_0 = Button(btn_frm, text="0")
btn_1 = Button(btn_frm, text="1")
btn_2 = Button(btn_frm, text="2")
btn_3 = Button(btn_frm, text="3")
btn_4 = Button(btn_frm, text="4")
btn_5 = Button(btn_frm, text="5")
btn_6 = Button(btn_frm, text="6")
btn_7 = Button(btn_frm, text="7")
btn_8 = Button(btn_frm, text="8")
btn_9 = Button(btn_frm, text="9")
btn_add = Button(btn_frm, text="+")
btn_sub = Button(btn_frm, text="-")
btn_div = Button(btn_frm, text="/")
btn_mult = Button(btn_frm, text="*")
btn_enter = Button(btn_frm, text="=")
btn_del = Button(btn_frm, text="Del")

# Debugging
inp_frm.grid(row=0, column=0)
btn_frm.grid(row=1, column=0)
btn_0.grid(row=4, column=0)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=0)
btn_3.grid(row=4, column=0)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=0)
btn_6.grid(row=3, column=0)
btn_7.grid(row=3, column=0)
btn_8.grid(row=2, column=0)
btn_9.grid(row=2, column=0)
btn_add.grid(row=2, column=0)
btn_sub.grid(row=2, column=0)
btn_div.grid(row=1, column=0)
btn_mult.grid(row=0, column=0)
btn_del.grid(row=0, column=0)
btn_enter.grid(row=0, column=0)

root_window.mainloop()