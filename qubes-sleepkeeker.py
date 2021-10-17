#!/usr/bin/env python3

# qubes-sleepkepper.py - automatic shutdown pc if no password provided after sleep
# EvaDogStar - github.com/evadogstar

import tkinter as tk
import sys
import os
#import argparse

def calcelShutdown():
	root.destroy()
	exit()
	pass

def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else:
    	label['text'] = 'shutdown now'
#    	os.system("shutdown /s /t 1") 
    	os.system("sudo shutdown now") 

	
#parser = argparse.ArgumentParser('sleepkeeper')
#parser.add_argument("post",action="store_true",help="just a flag argument")
#parser.add_argument("post",help="requested argument provided by the system")
#args = parser.parse_args()
#print (args.post)

try:
	if sys.argv[1] != 'post':
		exit()
except IndexError:
	exit()


root = tk.Tk()
root.title("Secure Shutdown")
#root.geometry("500x400")

##root.columnconfigure(0, minsize=200)
root.rowconfigure([0, 1, 2], minsize=50)

label = tk.Label(root, font=("Arial Bold", 36))
label.grid(column=0, row=1)

# call countdown first time    
countdown(100)

B = tk.Button(root, text ="Cancel Shutdown", font=("Arial Bold", 36), command = calcelShutdown)
B.grid(column=0, row=3)

root.mainloop()
