import tkinter
from functools import partial

def say_hi(word):
    def welcome():
        label.config(text='Hello %s' % word)
    return welcome

root = tkinter.Tk()
label = tkinter.Label(text='Hello world', font="25px")
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = MyButton(text='button2', command=say_hi('china'))
b2 = MyButton(text='button2', command=say_hi('Tedu'))
b3 = MyButton(text='quit', command=root.quit)
label.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
