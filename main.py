import tkinter as tk
from pwn import *
from ctfgui import *
from tkinter import ttk
from tkinter import * 

#button click functions
r = null
code = ''
def executeClick():
	code = interactive.get(1.0, "end")
	print(code)
	
def buttonClick():
	r = remote(hostInput.get(), int(portInput.get()))
	conn_and_exec(hostInput.get(), int(portInput.get()), r)
	print("Connecting..")
	
def send():

	string = interactive.get(1.0, "end")
	r.send(string.encode('utf-8'))
	r.recv()

def sendCode():
	try:	
		r.send(exec(code).encode('utf-8'))
	except:
		print("No connection established")
	print(exec(code))
	
#create root
root = Tk()

#set the elements for root
root.geometry('850x520')
root.configure(background='#F0F8FF')
root.title('PWN Gui')


#hostname and port connection inputs
Label(root, text='Hostname', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=100)

Label(root, text='Port', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=160)

hostInput=Entry(root)
hostInput.place(x=110, y=130)

portInput=Entry(root)
portInput.place(x=110, y=190)

connect = Button(root, text='Connect', command=buttonClick).place(x=110, y = 230)

isInteractive = IntVar()
isInjection = IntVar()
Checkbutton(root, text="Interactive Mode", variable=isInteractive, bg='#F0F8FF').place(x=110, y=300)
Checkbutton(root, text="Code Injection Mode", variable=isInjection, bg='#F0F8FF').place(x=110, y=330)

#connection and interactive code caching shell connection

Label(root, text='Connection Status', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=110, y=33300)
interactive = Text(root, height=15, width=60)
interactive.place(x=300, y=100)

execute = Button(root, text='Cache Code', command=executeClick).place(x=300, y = 370)
send = Button(root, text='Send', command=send).place(x=300, y=410)
sendCached = Button(root, text='Send Cached Code', command= sendCode).place(x=300, y=450)



root.mainloop()

