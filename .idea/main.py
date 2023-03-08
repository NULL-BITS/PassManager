from cryptography.fernet import Fernet
import linecache
import tkinter as tk
from tkinter import *
import os

Wrong = 0
Name = linecache.getline("config", 2)
if not os.path.exists('../.idea/config'):
    os.mknod('../.idea/config')


def writer(a,b,c):
    with open("config", 'r+') as conf:
        conf.write(a + "\n" + b + "\n" + c)


def setup():
    Valid = "yes "
    Name = input("Name: ")
    Password = input("Password: ")
    writer(Valid, Name, Password)
    Home()

def ViewPass():
        t = tk.Label(text=linecache.getline("config", 1))
        t.grid(row= 1, column=2, pady= 2)

def AddPass(a, b):
        App = a
        Password = b
        os.mknod('../.idea/.pass/' + App)
        open("../.idea/.pass/" + App, 'r+').write("App: " + App + "Pass: " + Password)


def Home():
        win = Tk()
        win.geometry("800x800")
        win.columnconfigure(10)
        win.rowconfigure(10)
        gen = tk.Button(text="Generate Pass")
        Add = tk.Button(text="Add Password", command=lambda : AddPass(input("App"), input("Password")))
        View = tk.Button(text="View Passwords", command=ViewPass())
        Dark = tk.Button(text="Darkmode", command=lambda: win.configure(background='black'))
        Dark.place(x=450, y= 10)
        gen.grid(row=2, column=1, pady=30, padx=10)
        Add.grid(row=3, column=1, pady=20, padx=10)
        View.grid(row=4, column=1, pady=20, padx=10)
        hi = Label(text="Hello there " + Name.__str__())
        hi.grid(row=1, column=1, padx= 10, pady=10)
        win.mainloop()



def start():
    check = open("config").read().count('yes', 0, 3)
    if(check == 0):
        setup()
    else:
        Home()


start()