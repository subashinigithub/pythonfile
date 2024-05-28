from tkinter import *
from tkinter import ttk,font
# from PIL import ImageTk,Image
import requests 

def train(trainno,win):
    win.destroy()
    win=Tk()
    win.geometry("400x400")
    base_url="https://rappid.in/apis/train.php?train_no={}".format(trainno)
    response=requests.get(base_url)
    train_status=response.json()
    Label(win,text="******************************************************").pack()
    Label(win,text="Train Name: "+train_status["train_name"])
    Label(win,text="******************************************************").pack()
    for station_info in train_status['data']:
        if station_info["is_current_station"]:
            Label(win,text="Now Station:\t\t "+station_info["station_name"]).pack()
            Label(win,text="Distance From the starting:\t "+station_info["distance"]).pack()
            Label(win,text="Timing:\t\t "+station_info["timing"]).pack()
            Label(win,text="Delay:\t\t "+station_info["delay"]).pack()
            Label(win,text="Platform No:\t\t "+station_info["platform"]).pack()
            Label(win,text="Halt Timing:\t\t "+station_info["halt"]).pack()
        else:
            Label(win,text=station_info["station_name"])
    Label(win,text="********************************************************").pack()
    Label(win,text="Msg: "+train_status["message"]).pack()
    Label(win,text="Messageupdated: "+train_status["updated_time"]).pack()
    Label(win,text="********************************************************").pack()
    win.mainloop()



def home():
    win=Tk()
    win.geometry("700x500")
    win.attributes("-fullscreen",True)
    frame=Frame(win,width=1500,height=60,bg="plum4")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Frame(win,width=1500,height=60,bg="green")
    f=Label(win,text="Track Train Location",font=label_font,bg="plum4",fg="black")
    f.place(relx=0.4,rely=0.00)

    f1=Frame(win,width=1000,height=50)
    f1.pack()
    f1.place(relx=0.3,rely=0.2)
    # img=ImageTk.PhotoImage(Image.open("train1.jpg"))
    # label=Label(f1,image=img)
    # label.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=25)
    l1=Label(win,text="Train No",bg="plum4",fg="black",font=label_font)
    l1.place(relx=0.4,rely=0.8)
    e1=Entry(win)
    e1.place(relx=0.53,rely=0.8,width=155,height=35)
    b=Button(win,text="Click",font=label_font,bg="green",fg="black",command=lambda:train(e1.get(),win))
    b.place(relx=0.5,rely=0.9)
    win.mainloop()
home()

