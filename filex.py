from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
from tkinter.font import Font
import mysql.connector
                             ####################################################################
def def2():
    root1 = Tk()
    root1.geometry("600x500")
    root1.title("Director")
    root1.resizable(0, 0)
    filename = ImageTk.PhotoImage(Image.open("photo1.jpeg"),master=root1)
    label = Label(root1, image=filename)
    label.place(x=0, y=0, relwidth=1,relheight=1)

    fonty = Font(root1,family="Times New Roman",size=18,weight = "bold",slant='italic')
    menu_font = Font(root1,family="Times New Roman",size=14,weight = "bold",slant='italic')
    button_font = Font(root1,family="Times New Roman",size=11,weight = "bold",slant='italic')

    label = Label(root1, text=" client information sheet",width=80,height=3,font=fonty,bg="#b3b3b3").place(x=55,y=10,relwidth=0.8,relheight=0.13 )

    text = Label(root1, text="DETAILS",width=20,font=fonty,bg="#b3b3b3")
    text.place(x=150,y=110)

    name1=StringVar()
    name2=StringVar()
    city=StringVar()
    adress=StringVar()
    phone=IntVar()
    filee=IntVar()
    order=IntVar()

    label = Label(root1,text="First_Name",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=191,width=130,height=24)
    entry1=Entry(root1,textvariable=name1)
    entry1.place(x=160, y=191,height=24,width=190)

    label = Label(root1,text="Last_Name",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=226,width=130,height=24 )
    entry2=Entry(root1,textvariable=name2)
    entry2.place(x=160, y=226,height=24,width=190)

    label = Label(root1,text="City",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=261,width=130,height=24 )
    entry3=Entry(root1,textvariable=city)
    entry3.place(x=160, y=261,height=24,width=190)

    label = Label(root1,text="Adress",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=296 ,width=130,height=24)
    entry4=Entry(root1,textvariable=adress)
    entry4.place(x=160, y=296,height=24,width=190)

    label = Label(root1,text="Phone_Num",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=330 ,width=130,height=24)
    entry5=Entry(root1,textvariable=phone)
    entry5.place(x=160, y=330,height=24,width=190)

    label = Label(root1,text="File_Num",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=371 ,width=130,height=24)
    entry6=Entry(root1,textvariable=filee)
    entry6.place(x=160, y=371,height=24,width=190)

    label = Label(root1,text="Fax_Num",width=13,font=menu_font,anchor=W,bg="#bfbfbf").place(x=26,y=408 ,width=130,height=24)
    entry7=Entry(root1,textvariable=order)
    entry7.place(x=160, y=408,height=24,width=190)
 ##################################""
    def add():
        e1 = name1.get()
        e2 = name2.get()
        e3 = city.get()
        e4 = adress.get()
        e5 = phone.get()
        e6 = filee.get()
        e7 = order.get()

        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "rootroot",database="company")
        my_cursor = mydb.cursor()
        #my_cursor.execute("TRUNCATE TABLE clients")#for clenig table rows
        #my_cursor.execute("CREATE TABLE clients(First_Name VARCHAR(255),Last_Name VARCHAR(255),Email VARCHAR(10),Adress VARCHAR(255),Phone_N INT(10),File_N INT(10),Order_Date INT(10))")
        stuff ="INSERT INTO clients(First_Name ,Last_Name ,Email ,Adress, Phone_N ,File_N ,Order_Date) VALUES (%s,%s,%s,%s,%s,%s,%s )"
        record = (e1,e2,e3,e4,e5,e6,e7)
        my_cursor.execute(stuff, record)

        mydb.commit()
        mydb.close()
       #####################################################
    def reset():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
    def retun():
        import file2
        file2.fun()
    Button(root1,text='ADD',width=10,font=button_font,command=add,bg="#cccccc").place(x=440, y=189)
    Button(root1,text='CLEAR',width=10,font=button_font,command=reset,bg="#cccccc").place(x=440, y=260)
    Button(root1,text='BACK',width=10,font=button_font,command=retun,bg="#cccccc").place(x=440, y=320)
    Button(root1,text='EXIT',width=10,font=button_font, command = root1.destroy,bg="#cccccc").place(x=440, y=390)

    root1.mainloop()
#def2()
