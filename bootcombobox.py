from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
""" Combobox()
c1=Combobox(win,values=['myd','trichy','tanjore'],bootstyle="dark")
c1.place(relx=0.02,rely=0.1) """

""" c1=Combobox(state="disabled")
c1.place(relx=0.02,rely=0.4)
cb=Combobox(win,text="disabled")
cb.place(relx=0.02,rely=0.5)
cb.configure(state="disabled")
"""
""" d1=DateEntry(win)
d1.place(relx=0.2,rely=0.1)
d2=DateEntry(win,bootstyle="Danger")
d2.place(relx=0.2,rely=0.2)
"""
""" #bootentry
e=Entry(win)
e.place(relx=0.2,rely=0.1)
e1=Entry(win,bootstyle="danger")
e1.place(relx=0.2,rely=0.2)
#disabled
e1=Entry(win,state="disabled")
e1.place(relx=0.2,rely=0.3)
e=Entry(win)
e.place(relx=0.2,rely=0.4)
e.configure(state="disabled")
#readonly
e1=Entry(win,state="readonly")
e1.place(relx=0.2,rely=0.5)
e=Entry(win)
e.place(relx=0.2,rely=0.6)
e.configure(state="readonly") """
#bootframe
""" f1=Frame(win,bootstyle="success",width=78,height=89)
f1.place(relx=0.2,rely=0.6) """
#floodgauge
""" f=Floodgauge(win)
f.place(relx=0.2,rely=0.5)
f1=Floodgauge(win,bootstyle="success",text="default")
f1.place(relx=0.2,rely=0.8)
 """
#boot menubutton
""" m=Menubutton(win,text="default")
m.place(relx=0.2,rely=0.1)
m1=Menubutton(win,bootstyle="success",text="default")
m1.place(relx=0.2,rely=0.2)
#outline
m=Menubutton(win,bootstyle="outline")
m.place(relx=0.2,rely=0.3)
m1=Menubutton(win,bootstyle="info-outline")
m1.place(relx=0.2,rely=0.4)
#diabled
m=Menubutton(win,state="disabled")
m.place(relx=0.2,rely=0.5)
b=Menubutton(win)
b.place(relx=0.2,rely=0.6)
b.configure(state="disabled") """
s=Separator(win)
s.place(relx=0.2,rely=0.5)
s1=Separator(win,bootstyle="success")
s1.place(relx=0.2,rely=0.9)
Sizegrip()
s2=Sizegrip(win,bootstyle="info")
s2.place(relx=0.2,rely=0.7)
win.mainloop()

