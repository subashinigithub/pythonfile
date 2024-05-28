from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import os 
import pymysql as mysql

def customerloginpage(data,win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.configure(bg="cyan4")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="maroon3")
    frame.pack()
    f=Frame(win,width=1500,height=60,bg="green")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="IOB BANK",font=label_font,bg="maroon3",fg="white")
    f.place(relx=0.4,rely=0.00)

    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    b=Label(win,text="Customer Loginpage",font=label_font,bg="cyan4",fg="black")
    b.place(relx=0.39,rely=0.15)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name "+data[0],font=label_font,bg="cyan4").place(relx=0.12,rely=0.3)
    l2=Label(win,text="Adhar No "+data[1],font=label_font,bg="cyan4").place(relx=0.4,rely=0.3)
    l3=Label(win,text="Pan No "+data[2],font=label_font,bg="cyan4").place(relx=0.7,rely=0.3)
    l4=Label(win,text="Contact "+data[3],font=label_font,bg="cyan4").place(relx=0.11,rely=0.5)
    l5=Label(win,text="Email-Id "+data[4],font=label_font,bg="cyan4").place(relx=0.4,rely=0.5)
    l6=Label(win,text="Address "+data[5],font=label_font,bg="cyan4").place(relx=0.7,rely=0.5)
    

    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    win.mainloop()


def customerlog(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.configure(bg="cyan4")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="maroon3")
    frame.pack()
    f=Frame(win,width=1500,height=60,bg="green")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="IOB BANK",font=label_font,bg="maroon3",fg="white")
    f.place(relx=0.4,rely=0.00)

    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    b=Label(win,text="Customer Login",font=label_font,bg="cyan4",fg="black")
    b.place(relx=0.35,rely=0.15)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="CustomerId",font=label_font,bg="cyan4",fg="black").place(relx=0.38,rely=0.3)
    l2=Label(win,text="Password",font=label_font,bg="cyan4",fg="black").place(relx=0.38,rely=0.4)
    e1=Entry(win)
    e1.place(relx=0.53,rely=0.31,width=140,height=30)
    e2=Entry(win)
    e2.place(relx=0.53,rely=0.41,width=140,height=30)

    def customerlogin1(win,a,b):
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="sksg")
        cursor=connection.cursor()
        result="select * from sr where Name='"+e1.get()+"'and Contact='"+e2.get()+"'"
        cursor.execute(result)
        print(result)
        r=0
        for x in cursor:
            customerloginpage(x,win)
            r=r+1
        if r>0:
            print("logged in")
        else:
            print("not logged")

        






    b=Button(win,text="Login",font=label_font,bg="green",fg="black",command=lambda:customerlogin1(win,e1.get(),e2.get()))
    b.place(relx=0.48,rely=0.6)

    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    win.mainloop()








def customerreg(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.configure(bg="cyan4")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="maroon3")
    frame.pack()
    f=Frame(win,width=1500,height=60,bg="green")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="IOB BANK",font=label_font,bg="maroon3",fg="white")
    f.place(relx=0.4,rely=0.00)

    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    b=Label(win,text="Customer Registration",font=label_font,bg="cyan4",fg="black")
    b.place(relx=0.35,rely=0.15)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font,bg="cyan4").place(relx=0.12,rely=0.3)
    l2=Label(win,text="Adhar No",font=label_font,bg="cyan4").place(relx=0.4,rely=0.3)
    l3=Label(win,text="Pan No",font=label_font,bg="cyan4").place(relx=0.7,rely=0.3)
    l4=Label(win,text="Contact",font=label_font,bg="cyan4").place(relx=0.11,rely=0.5)
    l5=Label(win,text="Email-Id",font=label_font,bg="cyan4").place(relx=0.4,rely=0.5)
    l6=Label(win,text="Address",font=label_font,bg="cyan4").place(relx=0.7,rely=0.5)
    name=Entry(win)
    name.place(relx=0.2,rely=0.3,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.5,rely=0.3,width=150,height=30)
    e3=Entry(win)
    e3.place(relx=0.78,rely=0.3,width=150,height=30)
    e4=Entry(win)
    e4.place(relx=0.2,rely=0.5,width=150,height=30)
    e5=Entry(win)
    e5.place(relx=0.5,rely=0.5,width=150,height=30)
    e6=Entry(win)
    e6.place(relx=0.78,rely=0.5,width=150,height=30)

    def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="sksg")
        cursor=connection.cursor()
        s="insert into sr(Name,AdharNo,PanNo,Contact,EmailId,Address)values(%s,%s,%s,%s,%s,%s)"
        t=(name.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("UserRegistration","Insert Successfully")
    def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="sksg")
        cursor=connection.cursor()
        sql="update sr set AdharNo='"+str(e2.get())+"',PanNo='"+str(e3.get())+"',Contact='"+str(e4.get())+"',EmailId='"+str(e5.get())+"',Address='"+str(e6.get())+"' where Name='"+name.get()+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("UserRegistration","Update Successfully")
    def delete():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="sksg")
        cursor=connection.cursor()
        sql="DELETE From sr WHERE Name='"+name.get()+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("UserRegistration","Delete Successfully")

    
        
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="update",font=label_font,bg="yellow",fg="black",command=lambda:update())
    b.place(relx=0.37,rely=0.7)
    b1=Button(win,text="insert",font=label_font,bg="green",fg="black",command=lambda:insert())
    b1.place(relx=0.47,rely=0.7)
    b2=Button(win,text="delete",font=label_font,bg="red",fg="black",command=lambda:delete())
    b2.place(relx=0.57,rely=0.7)
    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    win.mainloop()

def home():
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="maroon3")
    frame.pack()
    f2=Frame(win,width=350,height=890,bg="Hotpink1")
    f2.place(relx=0.0,rely=0.07)
    f=Frame(win,width=1500,height=50,bg="green")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="IOB BANK",font=label_font,bg="maroon3",fg="white")
    f.place(relx=0.4,rely=0.00)

    f1=Frame(win,width=1000,height=50)
    f1.pack()
    f1.place(relx=0.25,rely=0.07)
    img=ImageTk.PhotoImage(Image.open("nb.jpg"))
    label=Label(f1,image=img)
    label.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    a=Button(win,text="Customer Registration",bg='blue',fg='white',font=label_font,command=lambda:customerreg(win))
    a.place(relx=0.01,rely=0.6)
    b=Button(win,text="Customer Login",bg='blue',fg='white',font=label_font,command=lambda:customerlog(win))
    b.place(relx=0.03,rely=0.4)
    c=Button(win,text="Admin Login",bg='blue',fg='white',font=label_font,command=lambda:adminlog(win))
    c.place(relx=0.04,rely=0.2)

    c=Frame(win,width=1900,height=70,bg="maroon3")
    c.place(relx=0.001,rely=0.91)
    c1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    c1.place(relx=0.45,rely=0.92)
    win.mainloop()

home()
    

