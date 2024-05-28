from tkinter import *
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
win=Tk()
win.geometry("700x500")
frame=Frame(win,width=600,height=400)
frame.pack()
frame.place(relx=0.2,rely=0.2)
img=PhotoImage(Image.open("panda.jpg"))
label=Button(frame,image=img)
label.pack()
win.mainloop()