from tkinter import *
from tkinter import ttk
import random


root=Tk()
root.geometry('275x250+350+200')
root.title('EvenOrOdd')


button1 = ttk.Button(root, text='Play')
button1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
button2 = ttk.Button(root, text='Even')
button2.grid(row=3, column=0, padx=10, pady=20)
button3 = ttk.Button(root, text='Odd')
button3.grid(row=3, column=1, padx=10, pady=20)

v1=StringVar()
v2=StringVar()

e1 = Entry(root, textvariable=v1, width=40)
e1.grid(row=1, column=0, columnspan=2, padx=10)
e2 = Entry(root, textvariable=v2, width=20)
e2.grid(row=4, column=1, sticky=W)

label1 = Label(root, text='Is this number EVEN or ODD')
label1.grid(row=2, column=0, columnspan=2, padx=10)
label2 = Label(root, text='You are :')
label2.grid(row=4, column=0, padx=10,ipady=10, sticky=E)




def play(self):
    e1.delete(0,END)
    e2.delete(0,END)
    x=random.randrange(0,999)
    e1.insert(0,x)
    
def even(self):
    number=int(e1.get())
    if number % 2 == 0:
        e2.insert(0,'a Genius')
    else:e2.insert(0, 'a Failure')

def odd(self):
    number=int(e1.get())
    print(number)
    if (number%2 != 0):
        e2.insert(0,'a Genius')
    else: e2.insert(0, 'a Failure')


button1.bind('<ButtonPress>', play)
button2.bind('<ButtonPress>', even)
button3.bind('<ButtonPress>', odd)
