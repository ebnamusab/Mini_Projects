from tkinter import *
import random

root =Tk()
root.geometry('450x450')

l1 = Label(root,font=('Helvetica',260))
l1.pack()

def roll():
    dice = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text= f'{random.choice(dice)}')
    l1.pack

    b1 = Button(root,text="Roll",bg="Black",fg='white',command= roll, font=('Helvetica',25))
    b1.place(x=190, y=290)


roll()
root.mainloop()