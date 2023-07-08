from tkinter import *
import sqlite3
import random
import string
import datetime
import time
import os
from tkinter import ttk, Tk, Label, Entry, Button, messagebox, filedialog, END
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from io import BytesIO
from tkcalendar import DateEntry
from datetime import date 
from threading import *
from tkcalendar import Calendar
from captcha.image import ImageCaptcha


def raise_frame(frame):
    frame.tkraise()
    
root = Tk()
root.geometry('925x500+200+100')
root.resizable(0,0)
root.title('Academy Helpdesk System')

########################################## Add Materials (admin) ##################################################################
title=StringVar()
filename=StringVar()

def submit():
    global filename
    if title.get() == '' or filename.get() == '':
        messagebox.showerror("Error", "Please complete the required fields!")
    else:
        try:
            db = sqlite3.connect('academyhelpdesk.sqlite')
            cursor = db.cursor()
            cursor.execute("INSERT INTO material(Title, File) VALUES(?,?)", (title.get(), filename.get()))
            db.commit()
            db.close()
            messagebox.showinfo("Info", "A material has been successfully added.")
            title.set('')
            filename.set('')
        finally:
            title.set('')
            filename.set('')

add_materialsframe = Frame(root, width=925, height=500, bg='#FCE1F3')
add_materialsframe.place(x=0,y=0)
addNew = Label(add_materialsframe, text='Add New Materials', fg="Hotpink2",bg="#FCE1F3",font=("Time New Roman",26,"bold")).place(x=290,y=54)

title_label = Label(add_materialsframe, text='Material Title:', bg='#FCE1F3', font=('Times New Roman bold', 13)).place(x=200,y=200)
file_label = Label(add_materialsframe, text='Material File:', bg='#FCE1F3', font=('Times New Roman bold', 13)).place(x=200,y=300)

title_entry = Entry(add_materialsframe,width=40,textvariable=title).place(x=325,y=200)
file_entry = Entry(add_materialsframe, width=40,textvariable=filename).place(x=325, y=300)

Create_new=Button(add_materialsframe,text='Create New', bg="#F5FFFA",fg="black",border=0,font=('Times New Roman bold', 13), command=submit).place(x=400,y=420)

Button(add_materialsframe, width=8, pady=5, text="Home", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12), command=lambda: raise_frame(adminhomepage)).place(x=830, y=10)


################################################# Manage Materials Admin #########################################################################
def manage_materials():
    manage_materialframe = Frame(root, width=925, height=500, bg='#FCE1F3')
    manage_materialframe.place(x=0,y=0)

    managematerialtitle = Label(manage_materialframe, text="Manage Materials", fg="Hotpink2", bg="#FCE1F3",font=("Time New Roman", 26, "bold"))
    managematerialtitle.place(x=290, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=20, fieldbackground="#D3D3D3")
    style.map("Treeview", bg=[('selected', "#347083")])

    thetreeframe = Frame(manage_materialframe)
    thetreeframe.pack(padx=1, pady=275)

    treescroll = Scrollbar(thetreeframe)
    treescroll.pack(side=RIGHT, fill=Y)

    manage_tree = ttk.Treeview(thetreeframe, yscrollcommand=treescroll.set, selectmode="extended")
    manage_tree.pack()

    treescroll.config(command=manage_tree.yview)

    manage_tree['columns'] = ('1', '2')
    manage_tree['show'] = 'headings'

    manage_tree.column('1', width=400, anchor='c')
    manage_tree.column('2', width=500, anchor='c')

    manage_tree.heading('1', text='Material Title')
    manage_tree.heading('2', text='Material File')

    manage_tree.tag_configure('odd', background="lightblue")
    manage_tree.tag_configure('even', background="white")

    db = sqlite3.connect('academyhelpdesk.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM material")
    displayrecord = cursor.fetchall()

    global count
    count = 0
    for all in displayrecord:
        if count % 2 == 0:
            manage_tree.insert('', 'end', iid=count, values=(all[0], all[1]), tags=('even',))
        else:
            manage_tree.insert('', 'end', iid=count, values=(all[0], all[1]), tags=('odd',))
        count += 1

    entryframe = LabelFrame(manage_materialframe, text="Manage Materials")
    entryframe.place(x=3, y=50)

    titlemanageframe = Label(entryframe, text="Material Title")
    titlemanageframe.grid(row=0, column=0, padx=10, pady=10)
    managetitle_entry = Entry(entryframe, width=100)
    managetitle_entry.grid(row=0, column=1, padx=10, pady=10)

    filemanageframe = Label(entryframe, text="Material File")
    filemanageframe.grid(row=1, column=0, padx=10, pady=10)
    managefile_entry = Entry(entryframe, width=100)
    managefile_entry.grid(row=1, column=1, padx=10, pady=10)

    def update_data():
        if managetitle_entry.get() == "" or managefile_entry.get() == "":
            messagebox.showerror("Error", "Please do not leave any material details blank!")
        else:   
            select = manage_tree.focus()
            manage_tree.item(select, text="", values=(managetitle_entry.get(),managefile_entry.get()))            
            db = sqlite3.connect('academyhelpdesk.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE material SET Title=?, File=? WHERE Title=?", (managetitle_entry.get(), managefile_entry.get(), 
                                                                                 managetitle_entry.get()))
            db.commit()
            db.close()
            clearentry()
            messagebox.showinfo("Info", "The material details have been successfully updated.")

    def delete_data():
        if managetitle_entry.get() == "" or managefile_entry.get() == "":
            messagebox.showerror("Error", "Please do not leave any material details blank!")
        else:
            x=manage_tree.selection()[0]
            manage_tree.delete(x)

            db = sqlite3.connect('academyhelpdesk.sqlite')
            cursor = db.cursor()
            cursor.execute("DELETE from material WHERE Title=?", (managetitle_entry.get(),))
            db.commit()
            db.close()
            clearentry()
            messagebox.showinfo("Info", "The material has been deleted.")

    def clearentry():
        managetitle_entry.delete(0, END)
        managefile_entry.delete(0, END)

    def select_data(e):
        managetitle_entry.delete(0, END)
        managefile_entry.delete(0, END)

        select = manage_tree.focus()
        values = manage_tree.item(select, "values")

        managetitle_entry.insert(0, values[0])
        managefile_entry.insert(0, values[1])


    buttonframe = LabelFrame(manage_materialframe, text="Choose a button to manage")
    buttonframe.place(x=723, y=50)

    deletematerial = Button(buttonframe, text="Delete Material", command=delete_data)
    deletematerial.grid(row=0, column=0, padx=10, pady=10)

    editmaterial = Button(buttonframe, text="Update Material", command=update_data)
    editmaterial.grid(row=1, column=0, padx=10, pady=10)

    manage_tree.bind("<<TreeviewSelect>>", select_data)

    Button(manage_materialframe, width=8, pady=5, text="Home", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12), command=lambda: raise_frame(adminhomepage)).place(x=820, y=10)


############################################ view appointment ##############################################################
def appointment():
    view_appointmentframe = Frame(root, width=925, height=500, bg="#FCE1F3")
    view_appointmentframe.place(x=0, y=0)

    view_appointmenttitle = Label(view_appointmentframe, text="Appointment", fg="Hotpink2", bg="#FCE1F3",
                                  font=("Time New Roman", 26, "bold")).place(x=360, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=20, fieldbackground="#D3D3D3")
    style.map("Treeview", bg=[('selected', "#347083")])

    thetreeframe = Frame(view_appointmentframe)
    thetreeframe.pack(padx=1, pady=150)

    treescroll = Scrollbar(thetreeframe)
    treescroll.pack(side=RIGHT, fill=Y)

    manage_tree = ttk.Treeview(thetreeframe, yscrollcommand=treescroll.set, selectmode="extended")
    manage_tree.pack()

    treescroll.config(command=manage_tree.yview)

    manage_tree['column'] = ('1', '2', '3', '4', '5', '6')
    manage_tree['show'] = 'headings'

    manage_tree.column('1', width=150, anchor='c')
    manage_tree.column('2', width=250, anchor='c')
    manage_tree.column('3', width=100, anchor='c')
    manage_tree.column('4', width=100, anchor='c')
    manage_tree.column('5', width=150, anchor='c')
    manage_tree.column('6', width=150, anchor='c')

    manage_tree.heading('1', text='Username')
    manage_tree.heading('2', text='Appointment')
    manage_tree.heading('3', text='Time')
    manage_tree.heading('4', text='Date')
    manage_tree.heading('5', text='Venue')
    manage_tree.heading('6', text='PhoneNumber')

    manage_tree.tag_configure('odd', background="lightblue")
    manage_tree.tag_configure('even', background="white")

    db = sqlite3.connect('academyhelpdesk.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appointment")
    displayrecord = cursor.fetchall()

    global count 
    count = 0
    for all in displayrecord: 
        if count % 2 == 0:  
            manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('even',))
        else:
            manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('odd',))
        count += 1
    
    Button(view_appointmentframe, width=8, pady=5, text="Home", bg="#F5FFFA", fg="black", border=0,
           font=("Time New Roman", 12),
           command=lambda: raise_frame(adminhomepage)).place(x=820, y=10)

####################################################### admin homepage ##################################################################

adminhomepage=Frame(root,width=925,height=500,bg="#FCE1F3")
adminhomepage.place(x=0,y=0)

heading=Label(adminhomepage,text="Academy Helpdesk System",fg="Black",bg="White",font=("Time New Roman",26,"bold"))
heading.place(x=225,y=54)

btn1=Button(adminhomepage,width=30,pady=5,text="Add Materials",bg="White",fg="black",border=0,font=("Time New Roman",12), command=lambda:raise_frame(add_materialsframe)).place(x=130,y=170)
btn2=Button(adminhomepage,width=30,pady=5,text="Manage Materials",bg="White",fg="black",border=0,font=("Time New Roman",12), command = lambda:manage_materials()).place(x=130,y=320)
btn3 = Button(adminhomepage, width=30, pady=5, text="View Appointment", bg="White", fg="black", border=0, font=("Time New Roman", 12), command=appointment).place(x=520, y=320)


root.mainloop()

