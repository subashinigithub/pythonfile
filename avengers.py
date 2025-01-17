
import turtle
from tkinter import *
from tkinter import font,messagebox,ttk
from PIL import ImageTk,Image
import os
win=turtle.Screen()
s=turtle.Turtle()


#circle
s.penup()
s.setposition(0,-280)
s.pendown()
s.begin_fill()
s.color("blue")
s.pencolor("black")
s.circle(300)
s.end_fill()
s.penup()
s.setpos(160,105)
s.pendown()
s.left(170)
s.begin_fill()
s.color("white")
s.pencolor("black")
s.pensize(5)
s.speed(0)
for x in range(140):
    s.right(1)
    s.forward(1)
s.left(90)
for x in range(120):
    s.left(1)
    s.forward(3)
s.left(90)
for x in range(140):
    s.right(1)
    s.forward(1)
s.left(150)
s.forward(230)
s.right(60)
s.forward(80)
for x in range(160):
    s.right(1)
    s.forward(1)
s.right(25)
s.forward(90)
s.left(30)
for x in range(113):
    s.left(1)
    s.forward(1)
s.left(90)
for x in range(125):
    s.right(1)
    s.forward(1)
s.left(100)
for x in range(115):
    s.left(1)
    s.forward(3.5)
s.left(120)
for x in range(155):
    s.right(1)
    s.forward(1)
s.left(135)
s.forward(250)
s.right(70)
s.forward(90)
for x in range(150):
    s.right(1)
    s.forward(1)
s.right(25)
s.forward(90)
s.left(45)
for x in range(67):
    s.left(1)
    s.forward(2)
s.end_fill()
win.bye()

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

    def customerlogin1(a,b,win):
        f=open('banknew.txt',"r")
        lines=f.read().split("\n")
        for line in lines:
            data1=line.split("\t")
            a=e1.get()
            b=e2.get()
            if(data1[0]==a and data1[4]==b):
                customerloginpage(data1,win)


    b=Button(win,text="Login",font=label_font,bg="green",fg="black",command=lambda:customerlogin1(e1.get(),e2.get(),win))
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
    e1=Entry(win)
    e1.place(relx=0.2,rely=0.3,width=150,height=30)
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
    def file(a,b,c,d,win):
        f=open("banknew.txt",'a')
        f.write('\n')
        f.write(e1.get())
        f.write('\t')
        f.write(str(e2.get()))
        f.write('\t')
        f.write(str(e3.get()))
        f.write('\t')
        f.write(str(e4.get()))
        f.write('\t')
        f.write(str(e5.get()))
        f.write('\t')
        func1()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Register",font=label_font,bg="green",fg="black",command=lambda:file(e1.get(),str(e2.get()),str(e3.get()),str(e4.get()),win))
    b.place(relx=0.47,rely=0.7)

    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    win.mainloop()
def func1():
    messagebox.showinfo("IOB Bank","Register Successfully")
def adminpage(win):
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
    b=Label(win,text="Admin Login",font=label_font,bg="cyan4",fg="black")
    b.place(relx=0.39,rely=0.15)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font,bg="cyan4").place(relx=0.12,rely=0.3)
    l2=Label(win,text="Adhar No",font=label_font,bg="cyan4").place(relx=0.4,rely=0.3)
    l3=Label(win,text="Pan No",font=label_font,bg="cyan4").place(relx=0.7,rely=0.3)
    l4=Label(win,text="Contact",font=label_font,bg="cyan4").place(relx=0.11,rely=0.5)
    l5=Label(win,text="Email-Id",font=label_font,bg="cyan4").place(relx=0.4,rely=0.5)
    l6=Label(win,text="Address",font=label_font,bg="cyan4").place(relx=0.7,rely=0.5)
    e1=Entry(win)
    e1.place(relx=0.2,rely=0.3,width=150,height=30)
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
    def file(a,b,c,d,win):
        f=open("banknew.txt",'a')
        f.write('\n')
        f.write(e1.get())
        f.write('\t')
        f.write(str(e2.get()))
        f.write('\t')
        f.write(str(e3.get()))
        f.write('\t')
        f.write(str(e4.get()))
        f.write('\t')
        f.write(str(e5.get()))
        f.write('\t')
        func()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",font=label_font,bg="green",fg="black",command=lambda:file(e1.get(),str(e2.get()),str(e3.get()),str(e4.get()),win))
    b.place(relx=0.47,rely=0.7)

    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    
    win.mainloop()
def adminlogin(a,b,win):
    win.destroy()
    if(a=="suba" and b=="suba"):
        adminpage(win)
    else:
        print("Invalid Username or Password")
def adminlog(win):
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
    b=Label(win,text="Admin Login",font=label_font,bg="cyan4",fg="black")
    b.place(relx=0.4,rely=0.16)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Username",font=label_font,bg="cyan4",fg="black").place(relx=0.38,rely=0.3)
    l2=Label(win,text="Password",font=label_font,bg="cyan4",fg="black").place(relx=0.38,rely=0.4)
    e1=Entry(win)
    e1.place(relx=0.53,rely=0.31,width=140,height=30)
    e2=Entry(win)
    e2.place(relx=0.53,rely=0.41,width=140,height=30)
    b=Button(win,text="Login",font=label_font,bg="green",fg="black",command=lambda:adminlogin(e1.get(),e2.get(),win))
    b.place(relx=0.48,rely=0.6)

    a=Frame(win,width=1900,height=65,bg="maroon3")
    a.place(relx=0.001,rely=0.92)
    b1=Label(win,text="@Copyrights-2024",font=label_font,bg="maroon3",fg="white")
    b1.place(relx=0.45,rely=0.93)
    
    win.mainloop()


def func():
    messagebox.showinfo("IOB Bank","Login Successfully")

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
    















