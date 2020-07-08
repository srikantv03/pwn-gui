import tkinter as tk
from ctfgui import *
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box


def buttonClick():
	conn_and_exec(hostInput.get(), int(portInput.get()))
	print("Connecting..")

root = Tk()

# This is the section of code which creates the main window
root.geometry('850x520')
root.configure(background='#F0F8FF')
root.title('PWN Gui')



Label(root, text='Hostname', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=180)

Label(root, text='Port', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=240)


# This is the section of code which creates a text input box
hostInput=Entry(root)
hostInput.place(x=110, y=210)

portInput=Entry(root)
portInput.place(x=110, y=270)

connect = Button(root, text='Connect', command=buttonClick).place(x=110, y = 310)

Label(root, text='Connection Status', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=410)






root.mainloop()

