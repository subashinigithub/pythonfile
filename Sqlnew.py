from tkinter import *
from tkinter import ttk,font,messagebox 
import pymysql as mysql

def sqlogin(win,a,b):
    connection=mysql.connect(host="localhost",user="root",password="livewire",database="monk")
    cursor=connection.cursor()
    result="select * from  m4 where sname='"+a+"' and contact='"+b+"'"
    cursor.execute(result)
    print(result)
    r=0
    for x in cursor:
        print(x)
        r=r+1
    if r>0:
        print("loged in")
    else:
        print("not logged")


win=Tk()
win.geometry("700x500")
win.configure(bg="lightcoral")

win.attributes("-fullscreen",True)
frame=Frame(win,width=1500,height=60,bg="plum4")
frame.pack()
f=Frame(win,width=1500,height=60,bg="plum4")
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
f=Label(win,text="SQL LOGIN",font=label_font,bg="plum4",fg="black")
f.place(relx=0.4,rely=0.00)
b=Label(win,text="UserLogin",font=label_font,bg="lightcoral",fg="black")
b.place(relx=0.4,rely=0.16)

label_font=font.Font(weight="bold",family="Times New Roman",size=20)
l1=Label(win,text="UserName",font=label_font,bg="lightcoral",fg="black").place(relx=0.38,rely=0.3)
l2=Label(win,text="Contact",font=label_font,bg="lightcoral",fg="black").place(relx=0.38,rely=0.4)
e1=Entry(win)
e1.place(relx=0.53,rely=0.31,width=140,height=30)
e2=Entry(win)
e2.place(relx=0.53,rely=0.41,width=140,height=30)
b=Button(win,text="Login",bg="green",fg="black",font=label_font,command=lambda:sqlogin(win,e1.get(),str(e2.get())))
b.place(relx=0.48,rely=0.6)
win.mainloop()



















