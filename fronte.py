import tkinter as tk
import test
from tkinter import *
from PIL import Image, ImageTk

SN = ""
Key = ""
image = ""
master = tk.Tk()
master.geometry("1500x1000")


def show_entry_fields():
    print("Stonk Name: %s" % (e1.get()))
    SN = e1.get()
    Key = "OAPX1MWCR5GSEPXK"
    flag = test.st(SN, Key)
    if flag == "rise":
        image = "up.jpg"
    if flag == "fall":
        image = "down.jpg"

    load = Image.open(image)
    #load = load.resize(174, 290)
    render = ImageTk.PhotoImage(load)
    img = Label(master, image=render)
    img.image = render
    img.place(x=10, y=100)



tk.Label(master, text="Stonk Name").grid(row=0)
#tk.Label(master, text="Alphavantage Key").grid(row=1)

e1 = tk.Entry(master)
#e2 = tk.Entry(master)

e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)

tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
