""" import tkinter
root=tkinter.Tk()
root.mainloop()
 """
"""from tkinter import *
root=Tk()
root.geometry("200x200")
frame=Frame(root)
frame.pack()
root.mainloop()"""  


""" from tkinter import*
root=Tk()
frame=Frame(root,bg="grey",width=500,height=500)
frame.pack()
root.mainloop() """

""" import tkinter
from tkinter import messagebox
def hellocallBack():
    tkinter.messagebox.showwarning("Hello python","Hellow world")
top=tkinter.Tk()
B=tkinter.Button(top,text="new",command=lambda:hellocallBack())
B.pack()
top.mainloop() """

""" import tkinter
t=tkinter.Tk()
frame=tkinter.Frame(t,bg="green",width=400,height=400)
B=tkinter.Button(t,text="hello",activebackground="yellow")
frame.pack()
B.pack()
t.mainloop() """
""" from tkinter import *
root=Tk()
for fm in['pink','white','green','violet','blue','black']:
    Frame(height=20,width=640,bg=fm).pack()
root.mainloop() """
