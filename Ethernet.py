import subprocess
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Type Your OR Link")
window.geometry("250x200")
window.configure(background = "#0C090A")


def start_batch(): 
       subprocess.call([r'\Ethernet\Ethernet.bat'])

def Quit():
       window.destroy()

#Button
button = tk.Button(window, text="Open Ethernet", bg='black', fg='#54C571', command=start_batch)
button.grid(row=0,column=0,padx=85, pady=50)

button2 = tk.Button(window, text="Exit", bg='black', fg='#54C571', command=Quit)
button2.grid(row=1, padx=10, pady=10)

window.mainloop()
