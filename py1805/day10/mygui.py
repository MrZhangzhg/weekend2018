import tkinter
from functools import partial

root = tkinter.Tk()
label = tkinter.Label(text='Hello world', font="15px")
b1 = tkinter.Button(root, bg='blue', fg='white', text='button1')
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b2 = MyButton(text='button2')
b3 = MyButton(text='quit', command=root.quit)
label.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
