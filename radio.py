import tkinter
from tkinter import *
def sel():
    selection="you selected the option"+str(var.get())
    label.configure(text=selection)
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="male",variable=var,value=1,command=sel)
r1.pack()
r2=Radiobutton(root,text="female",variable=var,value=2,command=sel)
r2.pack()
r3=Radiobutton(root,text="others",variable=var,value=3,command=sel)
r3.pack(anchor=W)
label=Label(root)
label.pack()
root.mainloop()

