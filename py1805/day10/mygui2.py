import tkinter
from functools import partial

def hello():
    label.config(text='Hello china')

def welcome():
    label.config(text='hello tedu')

root = tkinter.Tk()
label = tkinter.Label(text='Hello world', font="25px")
b1 = tkinter.Button(root, bg='blue', fg='white', text='button1', command=hello)
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b2 = MyButton(text='button2', command=welcome)
b3 = MyButton(text='quit', command=root.quit)
label.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
