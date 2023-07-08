import tkinter as tk
import random
from tkinter import * 
from PIL import Image
from PIL import Image, ImageTk
from PyPDF2 import PdfFileReader
from tempfile import NamedTemporaryFile
import sqlite3
import os
from tkinter import messagebox
import webbrowser
import json
import subprocess
from tkinter import ttk
from threading import *

def main4():
    window = tk.Tk()
    window.state('zoomed')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    frame1 = tk.Frame(window)
    frame2 = tk.Frame(window)
    frame3 = tk.Frame(window)
    frame4 = tk.Frame(window)
    frame5 = tk.Frame(window)
    frame6 = tk.Frame(window)
    frame7 = tk.Frame(window)

    for frame in (frame1, frame2, frame3,frame4,frame5,frame6,frame7):
        frame.grid(row=0, column=0, sticky='nsew')

    #=======Image insertion===============
    logo_image = Image.open('D:\Pictures\pStuff\download1.png')  # Replace with the path to your logo image
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_image.resize((1200,1000))
    icon_image = Image.open('D:\Pictures\pStuff\FreeWebToolkit_1685639474.ico')
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_image.resize((80,80))
    CoA_image = Image.open("D:\Pictures\pStuff\CAA.jpg")  # Replace with the path to your logo image
    CoA_photo = ImageTk.PhotoImage(CoA_image)
    Math_image = Image.open("D:\Pictures\pStuff\Matg.jpg")  # Replace with the path to your logo image
    Math_photo = ImageTk.PhotoImage(Math_image)
    oop_image = Image.open("D:\Pictures\pStuff\pokemon.jpg")  # Replace with the path to your logo image
    oop_photo = ImageTk.PhotoImage(oop_image)
    tetris_image = Image.open("D:\Pictures\pStuff\ptetris.jpg")  # Replace with the path to your logo image
    tetris_photo = ImageTk.PhotoImage(tetris_image)

#============================================================

#=========Database Connection=================
    def show_frame(frame):
        frame.tkraise()

    def switch_to_subject_frame(frame):
        frame.tkraise()

    db = sqlite3.connect('academyhelpdesk.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appointment")
    displayrecord = cursor.fetchall()


# ==================Frame 1 code
    frame1_title = tk.Label(frame1, text='', font='times 35', bg='white')
    frame1_title.pack(fill='both', expand=True)
    frame1_logo = Label(frame1, image=logo_photo)
    frame1_logo.pack()
    frame1_logo.place(y=0)
    frame1_logo.config(width=1600,height=100)
    frame1_btn = tk.Button(frame1, text='Next Page', command=lambda: show_frame(frame2))
    frame1_btn.pack(fill='x', ipady=15)
    frame1_label = tk.Label(frame1 , text ="4004CEM Computer Architecture & Network" ,bg='white', font=("Arial",14))
    frame1_label.place(x=100,y=120)
    frame11=tk.Frame(frame1)
    frame11.config(height=520 , width=1600)
    frame11.place(x=10,y=150)
    frame1_label2 = tk.Label(frame1 , text ="4068CEM Mathematics For Computer Science" ,bg='white', font=("Arial",14))
    frame1_label2.place(x=600,y=120)
    frame1_label3 = tk.Label(frame1 , text ="4003CEM Object Oriented Programming" ,bg='white', font=("Arial",14))
    frame1_label3.place(x=1100,y=120)
    #Home Button
    def returnH():
        window.destroy()
        import ALL2_homepage
        ALL2_homepage.main3()

    rHButton = Button(frame1,text="Return Home",font=("Noto Sans",17),bg="red",fg="#FFFFFF",borderwidth=1,
                    command=(returnH))
    rHButton.place(x=1350,y=20)
    
#==================================

#==================================
    Modules3_button = tk.Button(frame11 ,image=oop_photo , command=lambda:show_frame(frame6))
    Modules3_button.place(x=1000, y=10)
    Modules3_button.config(height=500,width=500)


    Modules2_button = tk.Button(frame11 ,image=Math_photo , command=lambda:show_frame(frame5))
    Modules2_button.place(x=500, y=10)
    Modules2_button.config(height=500,width=500)


    Modules_button = tk.Button(frame11 ,image=CoA_photo , command=lambda:show_frame(frame4))
    Modules_button.place(x=10, y=10)
    Modules_button.config(height=500,width=500)
# ==================Frame 2 code

    def open_quiz():
        subprocess.run(["python" , "newnew.py"])
    def open_quiz2():
        subprocess.run(["python","new.py"])

    frame2_title = tk.Label(frame2, text='', font='times 35', bg='white')
    frame2_title.pack(fill='both', expand=True,anchor=N)
    frame2_btn = tk.Button(frame2, text='Next Page', command=lambda: show_frame(frame3))
    frame2_btn.pack(fill='x', ipady=15)
    quiz_btn=tk.Button(frame2,text="start quiz",command=open_quiz)
    quiz_btn.place(x=10,y=150)
    quiz_btn.config(width=50,height=14)
    quiz_btn2=tk.Button(frame2,text="start quiz2",command=open_quiz2)
    quiz_btn2.place(x=10,y=400)
    quiz_btn2.config(width=50,height=14)
    quiz_btn3=tk.Button(frame2,text="start quiz3",command=open_quiz2)
    quiz_btn3.place(x=400,y=150)
    quiz_btn3.config(width=50,height=14)
    quiz_btn4=tk.Button(frame2,text="start quiz4",command=open_quiz2)
    quiz_btn4.place(x=400,y=400)
    quiz_btn4.config(width=50,height=14)
    frame2_logo = Label(frame2, image=logo_photo)
    frame2_logo.pack()
    frame2_logo.place(y=0)
    frame2_logo.config(width=1600,height=100)
# ==================Frame 3 code
    def start_game():
        subprocess.run(["python" , "Tetris.py"])
    
    frame3_title = tk.Label(frame3, text='', font='times 35', bg='white')
    frame3_title.pack(fill='both', expand=True)
    frame3_button = tk.Button(frame3 , image=tetris_photo ,font=("Arial",20), command=start_game , bg="blue")
    frame3_button.config(width=700,height=600)
    frame3_button.place(x=200,y=150)
# Back to Frame 1 button
    def back_to_frame1():
        show_frame(frame1)

    back_btn = Button(frame3, text='Back', command=lambda :show_frame(frame7))
    back_btn.pack(fill='both')
    frame3_logo = Label(frame3, image=logo_photo)
    frame3_logo.pack()
    frame3_logo.place(y=0)
    frame3_logo.config(width=1600,height=100)
#=================Frame4 code

    back_btn1 = Button(frame4, text='Back', command=back_to_frame1)
    back_btn1.pack(anchor=N , fill='both')
    back_btn2 = Button(frame5, text='Back', command=back_to_frame1)
    back_btn2.pack(anchor=N , fill='both')
    back_btn3 = Button(frame6, text='Back', command=back_to_frame1)
    back_btn3.pack(anchor=N , fill='both')


    def view_pdf(file_path):
        try:
            webbrowser.open(file_path)
        except FileNotFoundError:
            messagebox.showerror("PDF Viewer", "File not found.")


    def load_pdf_files():
        folder_path1 = "D:\Documents\ProjectALL2\CA&N"
        folder_path2 = "D:\Documents\ProjectALL2\Maths"
        folder_path3 = "D:\Documents\ProjectALL2\OOP"  
        pdf_files1 = [f for f in os.listdir(folder_path1) if f.endswith('.pdf')]
        pdf_files2 = [f for f in os.listdir(folder_path2) if f.endswith('.pdf')]
        pdf_files3 = [f for f in os.listdir(folder_path3) if f.endswith('.pdf')]

        for file in pdf_files1:
            file_path = os.path.join(folder_path1, file)
            label = tk.Label(frame4, text=file, font=("Noto Sans", 25 * -1), cursor='hand2')
            label.pack(expand=True , fill='y')
            label.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

        for file in pdf_files2:
            file_path = os.path.join(folder_path2, file)
            label = tk.Label(frame5, text=file, font=("Noto Sans", 25 * -1), cursor='hand2')
            label.pack(expand=True , fill='y')
            label.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

        for file in pdf_files3:
            file_path = os.path.join(folder_path3, file)
            label = tk.Label(frame6, text=file, font=("Noto Sans", 25 * -1), cursor='hand2')
            label.pack(expand=True , fill='y')
            label.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))
    frame7_btn = tk.Button(frame7, text='back', command=lambda: show_frame(frame1))
    frame7_btn.pack(fill='x', ipady=15)
# ===================Frame 3 back to frame 2 code
    manage_tree = ttk.Treeview(frame7, selectmode="extended")
    manage_tree.pack()


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

    global count 
    count = 0
    for all in displayrecord: 
        if count % 2 == 0:  
            manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('even',))
        else:
            manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('odd',))
        count += 1


    #==================
    load_pdf_files()

    show_frame(frame1)
    window.mainloop()

if __name__ == "__main__":
    main4()