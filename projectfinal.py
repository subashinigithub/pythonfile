from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import os
import pymysql as mysql
def staffdetails(data,win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    d=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    d.place(relx=0.92,rely=0.006)


    img=ImageTk.PhotoImage(Image.open("reg2.jpg"))
    canvas=Canvas(win)
    canvas.create_image(600,330,image=img)
    canvas.pack(fill="both",expand=True)


    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
    

def staffloginpage(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)

    img=ImageTk.PhotoImage(Image.open("admin1.jpg"))
    canvas=Canvas(win)
    canvas.create_image(1020,330,image=img)
    canvas.pack(fill="both",expand=True)

    label_font=font.Font(weight="bold",family="Helvetica",size=20)
    canvas.create_text(300,160,text="Login",fill="blue",font=label_font)
    canvas.pack(fill="both",expand="True")
    label_font=font.Font(weight="bold",family="Helvetica",size=15)
    Username=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Username.place(relx=0.09,rely=0.4)
    Username.insert(0,'Username')
  
    f=Frame(win,width=294,height=2,bg="black").place(relx=0.09,rely=0.43)
    Password=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Password.place(relx=0.09,rely=0.5)
    Password.insert(0,'Password')
    g=Frame(win,width=294,height=2,bg="black").place(relx=0.09,rely=0.53)
    b=Button(win,text="Sign In",font=label_font,bg="skyblue",fg="black",height="1",width="7",command=lambda:stafflog(win,Username.get(),Password.get()))
    b.place(relx=0.17,rely=0.6)
    canvas.pack(fill="both",expand="True")
    def stafflog(win,a,b):
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
        cursor=connection.cursor()
        result="select * from mp where Name='"+str(Username.get())+"'and DOB='"+str(Password.get())+"'"
        cursor.execute(result)
        r=0
        for x in cursor:
            staffdetails(x,win)
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
def viewdetails(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    d=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    d.place(relx=0.92,rely=0.006)
    
    img=ImageTk.PhotoImage(Image.open("v.jpg"))
    canvas=Canvas(win)
    canvas.create_image(700,400,image=img)
 
    connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
    cursor=connection.cursor()
    result="select * from mp"
    cursor.execute(result)
    r=0
    xp=650
    yp=90
    for x in cursor:
        label_font=font.Font(weight="bold",family="Times New Roman",size=15)
        canvas.create_text(xp,yp,text=x,fill="black",font=label_font)
        xp+=10
        yp+=40

        canvas.pack(fill="both",expand=True)
    
        
   

    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
    


def particulardetails(data,win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.configure(bg="powderblue")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    d=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    d.place(relx=0.92,rely=0.006)

    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    l=Label(win,text="KNOW YOUR DETAILS",font=label_font,bg="powderblue",fg="black")
    l.place(relx=0.41,rely=0.15)


    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Emp-Id: " +str(data[0]),font=label_font,bg="powderblue").place(relx=0.3,rely=0.3)
    l2=Label(win,text="Name: "+data[1],font=label_font,bg="powderblue").place(relx=0.3,rely=0.4)
    l3=Label(win,text="DOB: "+data[2],font=label_font,bg="powderblue").place(relx=0.3,rely=0.5)
    l4=Label(win,text="Gender: "+data[3],font=label_font,bg="powderblue").place(relx=0.3,rely=0.6)
    l5=Label(win,text="Email-Id: "+data[4],font=label_font,bg="powderblue").place(relx=0.3,rely=0.7)
    l6=Label(win,text="Designation: "+data[5],font=label_font,bg="powderblue").place(relx=0.6,rely=0.3)
    l7=Label(win,text="Contact: "+data[6],font=label_font,bg="powderblue").place(relx=0.6,rely=0.4)
    l8=Label(win,text="Salary: "+data[7],font=label_font,bg="powderblue").place(relx=0.6,rely=0.5)
    l9=Label(win,text="Address:"+data[8],font=label_font,bg="powderblue").place(relx=0.6,rely=0.6)
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
def particular(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)

    img=ImageTk.PhotoImage(Image.open("staff6.jpg"))
    canvas=Canvas(win)
    canvas.create_image(700,400,image=img)
    canvas.pack(fill="both",expand=True)

    label_font=font.Font(weight="bold",family="Helvetica",size=20)
    canvas.create_text(200,160,text="Sign In",fill="powderblue",font=label_font)
    canvas.pack(fill="both",expand="True")
    label_font=font.Font(weight="bold",family="Helvetica",size=15)
    Username=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Username.place(relx=0.030,rely=0.4)
    Username.insert(0,'Username')
  
    f=Frame(win,width=294,height=2,bg="black").place(relx=0.030,rely=0.43)
    Password=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Password.place(relx=0.030,rely=0.5)
    Password.insert(0,'Password')

    g=Frame(win,width=294,height=2,bg="black").place(relx=0.030,rely=0.53)
    b=Button(win,text="Sign In",font=label_font,bg="powderblue",fg="black",height="1",width="7",command=lambda:particularlogin(win,Username.get(),Password.get()))
    b.place(relx=0.1,rely=0.6)
    canvas.pack(fill="both",expand="True")

    def particularlogin(win,a,b):
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
        cursor=connection.cursor()
        result="select * from mp where Name='"+str(Username.get())+"'and EmailId='"+str(Password.get())+"'"
        cursor.execute(result)
      
        r=0
        for x in cursor:
            particulardetails(x,win)
            
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()



def staffregister(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    d=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    d.place(relx=0.92,rely=0.006)


    img=ImageTk.PhotoImage(Image.open("reg3.jpg"))
    canvas=Canvas(win)
    canvas.create_image(750,459,image=img)
    canvas.pack(fill="both",expand=True)

    
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    t="***WELCOME TO STAFF-REGISTER***"
    canvas.create_text(360,45,text=t,fill="black",font=label_font)
    label_font=font.Font(weight="bold",family="Times New Roman",size=18)
    canvas.create_text(90,155,text="Emp-Id",fill="Black",font=label_font)
    canvas.create_text(90,225,text="Name",fill="Black",font=label_font)
    canvas.create_text(90,295,text="DOB",fill="Black",font=label_font)
    canvas.create_text(90,360,text="Gender",fill="Black",font=label_font)
    canvas.create_text(90,430,text="Email-Id",fill="Black",font=label_font)
    canvas.create_text(500,155,text="Designation",fill="Black",font=label_font)
    canvas.create_text(500,225,text="Contact",fill="Black",font=label_font)
    canvas.create_text(500,295,text="Salary",fill="Black",font=label_font)
    canvas.create_text(500,360,text="Address",fill="Black",font=label_font)

    canvas.pack(fill="both",expand=True)
    id=Entry(win)
    id.place(relx=0.13,rely=0.26,width=200,height=30)
    Name=Entry(win)
    Name.place(relx=0.13,rely=0.35,width=200,height=30)
    DOB=Entry(win)
    DOB.place(relx=0.13,rely=0.45,width=200,height=30)
    var=IntVar()
    g1=Radiobutton(win,text="Male",variable=var,value=1)
    g1.place(relx=0.13,rely=0.53)
    g2=Radiobutton(win,text="Female",variable=var,value=2)
    g2.place(relx=0.18,rely=0.53)
    g3=Radiobutton(win,text="Others",variable=var,value=3)
    g3.place(relx=0.24,rely=0.53)
    Email=Entry(win)
    Email.place(relx=0.13,rely=0.63,width=200,height=30)
    Designation=Entry(win)
    Designation.place(relx=0.43,rely=0.26,width=200,height=30)
    Contact=Entry(win)
    Contact.place(relx=0.43,rely=0.35,width=200,height=30)
    Salary=Entry(win)
    Salary.place(relx=0.43,rely=0.45,width=200,height=30)
    Address=Text(win)
    Address.place(relx=0.43,rely=0.53,width=200,height=60)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    a=Button(win,text="Insert",bg="grey",fg="black",font=label_font,command=lambda:insert())
    a.place(relx=0.2,rely=0.8)
    b=Button(win,text="Update",bg="grey",fg="black",font=label_font,command=lambda:update())
    b.place(relx=0.3,rely=0.8)
    c=Button(win,text="Delete",bg="grey",fg="black",font=label_font,command=lambda:Delete())
    c.place(relx=0.4,rely=0.8)
    def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
        cursor=connection.cursor()
        if(var.get()==1):
            gender="Male"
        elif(var.get()==2):
            gender="Female"
        elif(var.get()==3):
            gender="Others"
        s="insert into mp(EmpId,Name,DOB,Gender,EmailId,Designation,Contact,Salary,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(id.get(),Name.get(),DOB.get(),gender,Email.get(),Designation.get(),Contact.get(),Salary.get(),Address.get("1.0",END))
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("Employee-Register","Insert Successfully")
    def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
        cursor=connection.cursor()
        if(var.get()==1):
            gender="Male"
        elif(var.get()==2):
            gender="Female"
        elif(var.get()==3):
            gender="Others"
        sql="Update mp set EmpId='"+str(id.get())+"',Name='"+str(Name.get())+"',DOB='"+str(DOB.get())+"',gender='"+str(var.get())+"',EmailId='"+str(Email.get())+"',Designation='"+str(Designation.get())+"',Contact='"+str(Contact.get())+"',Address='"+str(Address.get("1.0",END))+"'where Name='"+str(Name.get())+"' "
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("Employee-Register","Update Successfully")
    def Delete():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="subiempmanage")
        cursor=connection.cursor()
        sql="Delete From mp where Name='"+str(Name.get())+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("Employee-Register","Deleted Successfully")
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()

def adminpage(win):
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=60,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=65,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.002)

    img=ImageTk.PhotoImage(Image.open("adminnxt.jpg"))
    canvas=Canvas(win)
    canvas.create_image(750,459,image=img)
    label_font=font.Font(weight="bold",family="Times New Roman",size=23)
    t="""     “A dream doesn't become reality through magic; it takes sweat, determination and hard work.”
            “No great achiever even those who made it seem easy ever succeeded without hard work.”
                                    “The way to get started is to quit talking and begin doing.”"""
    canvas.create_text(670,200,text=t,fill="black",font=label_font)
    canvas.pack(fill="both",expand=True)

    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    a=Button(win,text="Staff Register",bg="purple4",fg="white",font=label_font,command=lambda:staffregister(win))
    a.place(relx=0.62,rely=0.009)
    b=Button(win,text="View Details",font=label_font,bg="purple4",fg="white",command=lambda:viewdetails(win))
    b.place(relx=0.73,rely=0.009)
    c=Button(win,text="Particular",font=label_font,bg="purple4",fg="white",command=lambda:particular(win))
    c.place(relx=0.83,rely=0.009)
    d=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    d.place(relx=0.92,rely=0.006)


    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()


def adminlog(a,b,win):
    win.destroy()
    if(a=="subi" and b=="subi"):
        adminpage(win)
    else:
        print("Invalid Username or Password")

def admin(win):
    win.destroy()
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=70,bg="purple4")
    frame.pack()
    
    f2=Frame(win,width=1500,height=80,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.001)

    img=ImageTk.PhotoImage(Image.open("admin2.jpg"))
    canvas=Canvas(win)
    canvas.create_image(350,326,image=img)
    label_font=font.Font(weight="bold",family="Helvetica",size=20)
    canvas.create_text(1035,160,text="Login Your Account",fill="Green",font=label_font)
    canvas.pack(fill="both",expand="True")

    label_font=font.Font(weight="bold",family="Helvetica",size=15)
    Username=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Username.place(relx=0.65,rely=0.4)
    Username.insert(0,'Username')
    f=Frame(win,width=294,height=2,bg="black").place(relx=0.65,rely=0.43)
    Password=Entry(win,width=27,fg="black",border=0,bg="white",font=label_font)
    Password.place(relx=0.65,rely=0.5)
    Password.insert(0,'Password')
    g=Frame(win,width=294,height=2,bg="black").place(relx=0.65,rely=0.53)
    b=Button(win,text="Sign In",font=label_font,bg="green",fg="black",height="1",width="7",command=lambda:adminlog(Username.get(),Password.get(),win))
    b.place(relx=0.74,rely=0.6)
    canvas.pack(fill="both",expand="True")
    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
def exit(win):
    answer=messagebox.askquestion("exit","Do you want to exit the application?")
    if(answer=="yes"):
        win.destroy()
    

def home():
    win=Tk()
    win.geometry("700x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=70,bg="purple4")
    frame.pack()
    f1=Frame(win,width=1500,height=890,bg="plum4")
    f1.place(relx=0.0,rely=0.07)
    f2=Frame(win,width=1500,height=80,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=24)
    f2=Label(win,text="SHELL CARE",font=label_font,bg="purple4",fg="white")
    f2.place(relx=0.11,rely=0.002)
    img1=ImageTk.PhotoImage(Image.open("icon.jpg"))
    label=Label(image=img1,bg="purple4")
    label.place(relx=0.03,rely=0.001)

    img=ImageTk.PhotoImage(Image.open("img2.jpg"))
    label=Label(image=img)
    label.place(relx=0.0,rely=0.07)
    label_font=font.Font(weight="bold",family="Helvetica",size=15)
    a=Button(win,text="Admin Login",bg="purple4",fg="white",font=label_font,command=lambda:admin(win))
    a.place(relx=0.71,rely=0.006)
    b=Button(win,text="Staff Login",font=label_font,bg="purple4",fg="white",command=lambda:staffloginpage(win))
    b.place(relx=0.82,rely=0.006)
    c=Button(win,text="Exit",font=label_font,bg="purple4",fg="white",width=7,height=1,command=lambda:exit(win))
    c.place(relx=0.92,rely=0.006)

    label_font=font.Font(weight="bold",family="Times New Roman",size=22)
    d=Frame(win,width=1500,height=70,bg="purple4")
    d.place(relx=0.000,rely=0.935)
    e=Label(win,text="--@Copyrights 2024--",bg="purple4",fg="white",font=label_font)
    e.place(relx=0.39,rely=0.94)
    win.mainloop()
home()