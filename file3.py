from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
from tkinter.font import Font
import mysql.connector
                             ####################################################################
def def1():
    root1 = Tk()
    root1.geometry("600x500")
    root1.title("Director")
    root1.resizable(0, 0)
    filename = ImageTk.PhotoImage(Image.open("gray.jpg"),master=root1)
    label = Label(root1, image=filename)
    label.place(x=0, y=0, relwidth=1,relheight=1)

    fonty = Font(root1,family="Times New Roman",size=18,weight = "bold",slant='italic')
    menu_font = Font(root1,family="Times New Roman",size=14,weight = "bold",slant='italic')
    button_font = Font(root1,family="Times New Roman",size=11,weight = "bold",slant='italic')

    label = Label(root1, text=" Employee Information Card",width=80,height=3,font=fonty,bg="#d9d9d9").place(x=55,y=10,relwidth=0.8,relheight=0.13 )

    text = Label(root1, text="DETAILS",width=20,font=fonty,bg="#d9d9d9")
    text.place(x=150,y=110)

    name1=StringVar()
    name2=StringVar()
    birth=StringVar()
    sex=StringVar()
    salary=IntVar()
    emplo=IntVar()
    supper=IntVar()

    label = Label(root1,text="First_Name",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=190 ,width=130,height=24)
    entry1=Entry(root1,textvariable=name1)
    entry1.place(x=160, y=191,height=24,width=190)

    label = Label(root1,text="Last_Name",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=225,width=130,height=24 )
    entry2=Entry(root1,textvariable=name2)
    entry2.place(x=160, y=226,height=24,width=190)

    label = Label(root1,text="Birth_day",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=260,width=130,height=24 )
    entry3=Entry(root1,textvariable=birth)
    entry3.place(x=160, y=261,height=24,width=190)

    label = Label(root1,text="Gender",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=295,width=130,height=24 )
    entry4=Entry(root1,textvariable=sex)
    entry4.place(x=160, y=296,height=24,width=190)

    label = Label(root1,text="Salary",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=330,width=130,height=24 )
    entry5=Entry(root1,textvariable=salary)
    entry5.place(x=160, y=330,height=24,width=190)

    label = Label(root1,text="Empl_id",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=370 ,width=130,height=24)
    entry6=Entry(root1,textvariable=emplo)
    entry6.place(x=160, y=371,height=24,width=190)

    label = Label(root1,text="Supper_id",width=13,font=menu_font,anchor=W,bg="#d9d9d9").place(x=26,y=405,width=130,height=24 )
    entry7=Entry(root1,textvariable=supper)
    entry7.place(x=160, y=406,height=24,width=190)
 ##################################""
    def add():
        e1 = name1.get()
        e2 = name2.get()
        e3 = birth.get()
        e4 = sex.get()
        e5 = salary.get()
        e6 = emplo.get()
        e7 = supper.get()

        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "rootroot",database="company")
        my_cursor = mydb.cursor()
        #my_cursor.execute("TRUNCATE TABLE employees")
        #my_cursor.execute("CREATE TABLE employees(First_Name VARCHAR(255),Last_Name VARCHAR(255),Birth_day VARCHAR(10),Gender VARCHAR(255),Salary INT(10),EMP_id INT(10),SUP_id INT(10))")
        stuff ="INSERT INTO employees(First_Name ,Last_Name ,Birth_day ,Gender,Salary ,EMP_id ,SUP_id) VALUES (%s,%s,%s,%s,%s,%s,%s )"
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
    Button(root1,text='ADD',width=10,font=button_font,command=add,bg="#d9d9d9").place(x=440, y=189)
    Button(root1,text='CLEAR',width=10,font=button_font,command=reset,bg="#d9d9d9").place(x=440, y=260)
    Button(root1,text='BACK',width=10,font=button_font,command=retun,bg="#d9d9d9").place(x=440, y=320)
    Button(root1,text='EXIT',width=10,font=button_font, command = root1.destroy,bg="#d9d9d9").place(x=440, y=390)

    root1.mainloop()
#def1()
