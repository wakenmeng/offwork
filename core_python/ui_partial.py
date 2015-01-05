#coding: utf-8

from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, foreground='white', background='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', background='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title("PFAs")
root.mainloop()
