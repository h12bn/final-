from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
from tkinter.font import Font

def fun():
    root = Tk()
    root.title("Principle Page")
    root.geometry("700x500")
    root.minsize(350,150)
    root.resizable(False, False)
    frame = Frame(root)
    frame.place(relx=0, rely=0,relwidth=1,relheight=0.2)
    filename1 = ImageTk.PhotoImage(Image.open("plumes.jpg"),master=root)
    label1 = Label(frame, image=filename1)
    label1.place(x=0, y=0, relwidth=1, relheight=1)

    frame1 = Frame(root,bg="#e6e6e6")
    frame1.place(relx=0.1, rely=0.3,relwidth=0.8,relheight=0.7)
    fonty = Font(root,family="Times New Roman",size=25,weight = "bold",slant='italic')
    menu_font = Font(root,family="Times New Roman", size=10, weight="bold",slant='italic')
    text = Label(frame, text="The Main Page",width=20,font=fonty,bg="#d9d9d9")
    text.place(x=160,y=30)
    filename = ImageTk.PhotoImage(Image.open("plumes.jpg"),master=root)
    label = Label(frame1, image=filename)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def info():
        import file3
        file3.def1()
    def home():
        import loging
    def client():
        import filex
        filex.def2()
    def c_data():
        import file1
        file1.def3()
    def e_data():
        import tk3
        tk3.def4()

    Btn1 = Button(frame1,text='Home',width=20,height=8,relief=FLAT,font=menu_font,command=home,bg="#bfbfbf").place(x=35, y=30)

    Button(frame1,text='Info_Card',width=20,height=8,relief=FLAT,font=menu_font,command= info,bg="#bfbfbf").place(x=200, y=30)
    Label(frame1,bg="#bfbfbf").place(x=200, y=30)

    Button(frame1,text='Employees',width=20,height=8,relief=FLAT,font=menu_font,command=e_data,bg="#bfbfbf").place(x=370, y=30)
    Label(frame1,bg="#bfbfbf").place(x=370, y=30)

    Button(frame1,text='Clients',width=20,height=8,relief=FLAT,font=menu_font,command=client,bg="#bfbfbf").place(x=37, y=190)
    Label(frame1,bg="#bfbfbf").place(x=37, y=190)

    Button(frame1,text='Client Data',width=20,height=8,relief=FLAT,font=menu_font,command=c_data,bg="#bfbfbf").place(x=200, y=190)
    Label(frame1,bg="#bfbfbf").place(x=200, y=190)

    Button(frame1,text='Exit',width=20,height=8,relief=FLAT,font=menu_font, command = root.destroy,bg="#bfbfbf").place(x=370, y=190)
    Label(frame1,bg="#bfbfbf").place(x=370, y=190)

    root.mainloop()
#fun()
