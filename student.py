import tkinter
from tkinter import *
r=Tk()
r.geometry("200x200")
var=IntVar()
l1=Label(r,text="Name")
l1.grid(row=0,column=1)
l2=Label(r,text="Age")
l2.grid(row=1,column=1)
l3=Label(r,text="gender")
l3.grid(row=2,column=1)
l4=Label(r,text="physicallychallenged")
l4.grid(row=3,column=1)
l5=Label(r,text="sportsquota")
l5.grid(row=4,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Radiobutton(r,text="male",variable=var,value=1)
e3.grid(row=2,column=2)
e4=Radiobutton(r,text="female",variable=var,value=2)
e4.grid(row=3,column=2)
e5=Radiobutton(r,text="others",variable=var,value=3)
e5.grid(row=4,column=2)
checkvar1=IntVar()
checkvar2=IntVar()
e6=Checkbutton(r,text="yes",variable=checkvar1,onvalue=1,offvalue=0,height=1,width=20)
e6.grid(row=5,column=2)
e7=Checkbutton(r,text="No",variable=checkvar2,onvalue=1,offvalue=0,height=1,width=20)
e7.grid(row=6,column=2)
r.mainloop()







