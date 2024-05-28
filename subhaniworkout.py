#checkbutton
import tkinter
from tkinter import *
root=Tk()
""" checkvar1=IntVar()
checkvar2=IntVar()
c1=Checkbutton(root,text="Music",variable=checkvar1,onvalue=1,offvalue=0,height=1,width=20)
c2=Checkbutton(root,text="video",variable=checkvar2,onvalue=1,offvalue=0,height=1,width=20)
c1.pack()
c2.pack()
root.mainloop() """
#radiobutton
""" def sel():
    selection="you selected the option" + str(var.get())
    label.configure(text=selection) """

var=IntVar()
r1=Radiobutton(root,text="male",variable=var,value=1)
r1.pack()
r2=Radiobutton(root,text="female",variable=var,value=2)
r2.pack()
r3=Radiobutton(root,text="transgender",variable=var,value=3)
r3.pack()

root.mainloop()