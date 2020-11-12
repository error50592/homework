from tkinter import *
import tkinter as tk
import random

def btn_click(event):
    l1.config(text=random.randint(1,1001))
    l2.config(text=random.randint(1,1001))
    l3.config(text=random.randint(1,1001))

root = Tk()
#root['bg']='#000000'
root.title("однорукий бандит")
root.geometry('200x200')
root.resizable(width=False,height=False)

btn1=tk.Button(root,text='кнопка',bg="#708090",activebackground='#000000',font=("Verdana", 13))
root.bind('<Button-1>', btn_click)
btn1.pack()

l1 = Label(text=random.randint(1,1001), font="Arial 14")
l2 = Label(text=random.randint(1,1001),font="Arial 14")
l3 = Label(text=random.randint(1,1001),font="Arial 14")
l1.pack()
l2.pack()
l3.pack()

root.mainloop()
