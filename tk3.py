from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
from tkinter.font import Font
import mysql.connector

def def4():
        root1 = Tk()
        root1.resizable(0, 0)
        root1.geometry("860x480")
        root1.title("Employees Data")
        filename = ImageTk.PhotoImage(Image.open("wow.jpg"),master=root1)
        label = Label(root1, image=filename)
        label.place(x=0, y=0, relwidth=1,relheight=1)
        fonty = Font(root1,family="Times New Roman",size=18,weight = "bold",slant='italic')
        menu_font = Font(root1,family="Times New Roman",size=12,weight = "bold",slant='italic')
        button_font = Font(root1,family="Times New Roman",size=11,weight = "bold",slant='italic')
        label = Label(root1, text=" Employees Information Database",width=80,height=3,font=fonty,bg="#d9d9d9").place(x=90,y=10,relwidth=0.8,relheight=0.13 )

        def show():
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "rootroot",database="company")
            my_cursor = mydb.cursor()
            my_cursor.execute("SELECT * FROM employees")
            records = my_cursor.fetchall()
            #print(*records)
            print_records = ""
            for record in records:
                print_records += str(record[0])+'\t'+'\t'+ str(record[1])+'\t'+'\t'+str(record[2])+'\t'+str(record[3])+'\t'+'\t'+str(record[4])+'\t'+'\t'+str(record[5])+'\t'+'\t'+str(record[6])+'\t'+'\t'+ "\n"

            label2 = Label(root1,label,font=menu_font,bg="#f2f2f2",text="First_Name\tLast_name\tBirth_day\tGender\t\t Salary\t\tEmp_id\t\tSupper_id\t\t").place(x=0,y=190)
            query = Label(root1,text=print_records,font=menu_font,anchor=W,bg="#f2f2f2")
            query.place(x=0, y=226)

            mydb.commit()
            mydb.close()
        Button(root1,text='SHOW RECORDS',width=30,font=button_font,command=show,bg="#d9d9d9").place(x=290, y=120)
        root1.mainloop()
#def4()
