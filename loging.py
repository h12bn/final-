from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
from tkinter.font import Font
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
root.title("Director")
root.resizable(0, 0)
filename = ImageTk.PhotoImage(Image.open("design.jpg"),master=root)
label = Label(root, image=filename)
label.place(x=0, y=0, relwidth=1,relheight=1)
label.image = filename
fonty = Font(root,family="Times New Roman",size=20,weight = "bold",slant='italic')
menu_font = Font(root,family="Times New Roman",size=13,weight = "bold",slant='italic')
button_font = Font(root,family="Times New Roman",size=10,weight = "bold",slant='italic')
headingFrame1 = Label(root,bg='#455A64',font=fonty,bd=5, text="COMPANY WEBSITE")
headingFrame1.place(x=70,y=26,relwidth=0.7,relheight=0.13)
label = Label(root,text="Fullname",width=20,font=menu_font).place(x=40,y=110 )
entry=Entry(root).place(x=200, y=113)
label1 = Label(root,text=" Password",width=20,font=menu_font).place(x=35,y=140)
entry1=Entry(root).place(x=200, y=143)

def register():
    import file2
    file2.fun()

Btn = Button(root,text="Search",bg='#264348', fg='white')
Btn.place(x=150, y=180, relwidth=0.18,relheight=0.08)
Btn.config(command= register,font=menu_font)
quitBtn = Button(root,text="Quit",bg='#455A64', fg='white',font=menu_font, command=root.destroy)
quitBtn.place(x=250, y=180, relwidth=0.18,relheight=0.08)
messagebox.showinfo("Information","I Wich you will like it dear brother")
root.mainloop()
