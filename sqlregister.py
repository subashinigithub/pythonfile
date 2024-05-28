from tkinter import *
from tkinter import ttk,font,messagebox
import pymysql as mysql
win=Tk()
win.geometry("500x500")
win.attributes('-fullscreen',True)
win.configure(bg="lightcoral")
frame=Frame(win,width="1500",height=60,bg="violetred")
frame.pack()

f=Frame(win,width="1500",height=60,bg="violetred")
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
f=Label(win,text="STUDENT REGISTRATION",font=label_font,bg="violetred",fg="white")
f.place(relx=0.35,rely=0.00)
label_font=font.Font(weight="bold",family="Tahoma",size=20)
l1=Label(win,text="S_Id",font=label_font,bg="lightcoral",fg="black")
l1.place(relx=0.4,rely=0.2)
l2=Label(win,text="Name",font=label_font,bg="lightcoral",fg="black")
l2.place(relx=0.4,rely=0.3)
l3=Label(win,text="FatherName",font=label_font,bg="lightcoral",fg="black")
l3.place(relx=0.4,rely=0.4)
l4=Label(win,text="Contact",font=label_font,bg="lightcoral",fg="black")
l4.place(relx=0.4,rely=0.5)
l5=Label(win,text="Email_ID",font=label_font,bg="lightcoral",fg="black")
l5.place(relx=0.4,rely=0.6)
l6=Label(win,text="Address",font=label_font,bg="lightcoral",fg="black")
l6.place(relx=0.4,rely=0.7)
e1=Entry(win)
e1.place(relx=0.55,rely=0.2,width=150,height=30)
e2=Entry(win)
e2.place(relx=0.55,rely=0.3,width=150,height=30)
e3=Entry(win)
e3.place(relx=0.55,rely=0.4,width=150,height=30)
e4=Entry(win)
e4.place(relx=0.55,rely=0.5,width=150,height=30)
e5=Entry(win)
e5.place(relx=0.55,rely=0.6,width=150,height=30)
e6=Entry(win)
e6.place(relx=0.55,rely=0.7,width=150,height=30)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)

def insert():
    connection=mysql.connect(host="localhost",user="root",password="livewire",database="subireg")
    cursor=connection.cursor()
    s="insert into subr(Name,FatherName,Contact,Email_ID,Address) values (%s,%s,%s,%s,%s)"
    t=(e2.get(),e3.get(),e4.get(),e5.get(),e6.get())
    cursor.execute(s,t)
    
    
    connection.commit()
    messagebox.showinfo("studentregistration","insert successfully")
def update():
    connection=mysql.connect(host="localhost",user="root",password="livewire",database="subireg")
    cursor=connection.cursor()
    s="update subr set Name='"+str(e2.get())+"',FatherName='"+str(e3.get())+"',Contact='"+str(e4.get())+"',Email_Id='"+str(e5.get())+"',Address='"+str(e6.get())+"' where S_Id={}".format(int(e1.get()))
    cursor.execute(s)  
    connection.commit() 
    messagebox.showinfo("studentregistration","update successfully")
def delete():
    connection=mysql.connect(host="localhost",user="root",password="livewire",database="subireg")
    cursor=connection.cursor()
    k="DELETE From subr WHERE S_Id={}".format(int(e1.get()))
    cursor.execute(k)
    connection.commit()
    messagebox.showinfo("studentregistration","deleted successfully")



b1=Button(win,text="insert",font=label_font,bg="green",fg="black",command=lambda:insert())
b1.place(relx=0.3,rely=0.8)
b2=Button(win,text="update",font=label_font,bg="yellow",fg="black",command=lambda:update())
b2.place(relx=0.45,rely=0.8)
b3=Button(win,text="delete",font=label_font,bg="red",fg="black",command=lambda:delete())
b3.place(relx=0.6,rely=0.8)





win.mainloop()