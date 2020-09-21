try:
	import sys
	import os
	import time
	import random
	import pynput
	import threading
	import tkinter as tk
	from tkinter import *
	from pynput.keyboard import Key, Controller as KeyboardController
except ImportError as err:
	print("couldnt load module: " + str(err))
	sys.exit(2)


# NOTES/BUGS

# also put some time restrictions and word restrictions	
# data types need to be changed after
# when started it will run the pynput twice
# GUI user guidance general polishing ect

os.system("cls")
keyboardcontroller = KeyboardController()

t = 0
w = ""
b = False

# FRONT END WITH TKINTER ~ very crappy gui

root = tk.Tk()

# pynput wud be written in this function
def main():
	global b,t,w

	if b == True:
		print("passed to main function")
		print(t, w, b)

		wl = list(w)
		print(wl)

		for x in wl:
			keyboardcontroller.press(x)
			keyboardcontroller.release(x)

		keyboardcontroller.press(Key.enter)
		keyboardcontroller.release(Key.enter)


		root.after(t, main)
	elif b == False:
		pass

def startfnc():
	global b,t,w
	print("passed to start function")
	b = True
	t = txtlbl.get()
	w = timelbl.get()
	print(t, w, b)
	main()

def stopfnc():
	global b,t,w
	print("passed to stop function")
	b = False
	print(t, w, b)


root.title("Nathaniels SpamBot 3000")
canvas = tk.Canvas(root, height=400, width=400, bg="white").pack()
frame = tk.Frame(root, bg="#263D42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
startbtn = tk.Button(frame, text="Start",  fg="white", bg="#263D42", command=startfnc).pack()
stopbtn = tk.Button(frame, text="Stop",  fg="white", bg="#263D42", command=stopfnc).pack() 

txtvar=tk.StringVar()
txtvar.set("")

timevar=tk.StringVar()
timevar.set("") 

txtlabel = tk.Label(frame, text="insert time in miliseconds")
txtlabel.pack()
txtlbl = tk.Entry(frame, textvariable=txtvar, font=("Calibre",10,"normal"))
txtlbl.pack()

timelabel = tk.Label(frame, text="insert text you want to spam")
timelabel.pack()
timelbl = tk.Entry(frame, textvariable=timevar, font=("Calibre",10,"normal"))
timelbl.pack()

if b == True:
	root.after(t, main)

root.mainloop()




"""
thread1 = threading.Thread(target=main)
thread1.start()
thread2 = threading.Thread(target=root)
thread2.start()
"""