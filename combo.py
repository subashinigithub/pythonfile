from tkinter import *
from tkinter import ttk
root=Tk()
root.title("combobox example")
root.geometry("800x800")
combo=ttk.Combobox(root,values=['a','b','c'])
combo.set("choices")
combo.place(relx=0.6,rely=0.6)
combo.pack()
def option_selected(event):
    selected_option=combo.get()
    print("you selected:",selected_option)
combo.bind("<<ComboboxSelected>>",option_selected)
root.mainloop()