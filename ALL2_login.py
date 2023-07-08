from tkinter import *
import sqlite3
import random
import string
from tkinter import Tk, Label, Entry, Button, messagebox, END
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image


def main1():
    root1 = Tk()
    root1.geometry('925x500+200+100')
    root1.resizable(0,0)
    root1.title('Academy Helpdesk System')

    ################################################## Image ########################################
    img=PhotoImage(file="D:/Pictures/pStuff/login.png")
    Label(root1,image=img,bg="white", width=450, height=500).place(x=0,y=0)

    ################################################### Frame ##########################################
    l = Frame(root1)
    w = Frame(root1)

    ############################################### String Variable ############################################################
    nameinput = StringVar()
    emailinput = StringVar()

    #################################################### Database #################################################################### 
    def database():
        global db, cursor
        db=sqlite3.connect('academyhelpdesk.sqlite')
        cursor = db.cursor()

    
    #################################################### Login ####################################################################
    def Login():
        database()
        if e1.get() == '' or e2.get() == '' :
            messagebox.showerror('Error', 'Please complete the required field !')
        elif e1.get() == "Admin12345" and e2.get() == "Admin12345" :
            messagebox.showinfo("Info", "Welcome Back Admin")
            root1.destroy()
            import ALL2_admin
            
        else:       
            cursor.execute("SELECT * FROM user WHERE Username = ? and Password = ?", (e1.get(), e2.get()))
            if cursor.fetchone() is not None :
                messagebox.showinfo('Info', 'Login Successfully')
                root1.destroy()
                import ALL2_homepage
                ALL2_homepage.main3()
                
                
            else:
                messagebox.showerror('Error', 'Invalid username or password')
                db.commit()

    #################################################### Register ####################################################################
    def check_and_register():
        
        verify_label.grid_forget()

        if registername.get() == '' or registeremail.get() == '' or registerpassword.get() == '' or confirmpassword.get() == '':
            messagebox.showerror('Error', 'Please complete the required field!')
        elif registerpassword.get() != confirmpassword.get():
            messagebox.showerror('Error', 'Password does not match!')
        elif len(registerpassword.get()) < 4 or len(confirmpassword.get()) < 4:
            messagebox.showerror('Error', 'Password must be at least 5 characters!')
        elif entry.get().lower() != random_string.lower():
            messagebox.showerror('Error', 'Captcha does not match!')
            createImage()
        else:
            database()
            test = cursor.execute("SELECT Email FROM user WHERE Email=?", (registeremail.get(),))
            if cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Account has been registered!')
            else:
                cursor.execute("INSERT INTO user(Username, Email, Password) VALUES(?,?,?)", (registername.get(), registeremail.get(), registerpassword.get()))
                l.tkraise()
                db.commit()
                db.close()
                messagebox.showinfo('Info', 'Register Successfully')


    def createImage(flag=0):
        global random_string
        global image_label
        global image_display
        
        if flag == 1:
            verify_label.grid_forget()
        
        entry.delete(0, END)
        
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        image_captcha = ImageCaptcha(width=200, height=100)
        image_generated = image_captcha.generate(random_string)
        image_display = ImageTk.PhotoImage(Image.open(image_generated))
        
        if 'image_label' in locals():
            image_label.grid_forget()

        image_label = Label(w, image=image_display)
        image_label.grid(row=1, column=0, columnspan=2, padx=10)
        image_label.place(x=240,y=130)


            
    ################################################## GUI ##############################################
    #loginpage
    l=Frame(root1,width=475,height=500,borderwidth=1,bg="white")
    l.place(x=450,y=0)
    logibtitle=Label(l, text='Log In',fg="#57a1f8",bg="white",font=("Arial" , 23 , "bold")).place(x=200,y=10)

    # Entry for username
    l1=Label(l, text="Username", fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l1.place(x=75,y=45)
    e1=Entry(l,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11))
    e1.place(x=80,y=70)
    e1.insert(0,'')
    Frame(l,width=205 , height=2 , bg="black").place(x=75,y=95)
                    
    # Entry for password 
    l2=Label(l, text="Password" , fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l2.place(x=75,y=115)
    e2=Entry(l,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11),show="*")
    e2.place(x=80,y=140)
    e2.insert(0,"")
    Frame(l ,width=205 , height=2 , bg="black").place(x=75,y=165)

    # Login button       
    loginbtn=Button(l,text="Login" ,command =Login , bg="#57a1f8",fg="white" ,cursor="hand2")
    loginbtn.config(padx=80)
    loginbtn.place(x=80,y=200)


    

    #registerpage
    w=Frame(root1,width=475,height=500,borderwidth=1,bg="white")
    w.place(x=450,y=0)
    Registertitle=Label(w, text="Sign Up",fg="#57a1f8",bg="white",font=("Arial" , 23 , "bold")).place(x=200,y=10)

    # Entry for username
    l3=Label(w, text="Username" , fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l3.place(x=10,y=100)
    registername=Entry(w,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11))
    registername.place(x=15,y=130)
    registername.insert(0,"")
    Frame(w,width=205 , height=2 , bg="black").place(x=5,y=150)
                
    # Entry for email
    l4=Label(w, text="Email" , fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l4.place(x=10,y=160)
    registeremail=Entry(w,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11))
    registeremail.place(x=15,y=190)
    registeremail.insert(0,"")
    Frame(w,width=205 , height=2 , bg="black").place(x=5,y=210)
        
    # Entry for password
    l5=Label(w, text="Password" , fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l5.place(x=10,y=220)
    registerpassword=Entry(w,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11),show="*")
    registerpassword.place(x=15,y=250)
    registerpassword.insert(0,"")
    Frame(w,width=205 , height=2 , bg="black").place(x=5,y=270)

    # Entry for confirm password
    l6=Label(w, text="Confirm password" , fg="#57a1f8" , bg="white" , font = ("Arial" , 12 ))
    l6.place(x=10,y=280)
    confirmpassword=Entry(w,width=25 , fg='black',borderwidth=0, bg='white' , font = ("Arial" , 11),show="*")
    confirmpassword.place(x=15,y=310)
    confirmpassword.insert(0,"")
    Frame(w,width=205 , height=2 , bg="black").place(x=5,y=330)

    #Captcha image
    verify_label = Label(w)
    image_label = Label(w)
    verify_label = Label(w, text="Captcha", fg="#57a1f8", bg="white", font=("Arial", 12))
    verify_label.place(x=250, y=100)

    entry = Entry(w, width=15, borderwidth=3, font=("Arial", 11))
    entry.place(x=250, y=250)
    createImage()

    path = "D:/Pictures/pStuff/textcaptcha.png"
    reload_img = ImageTk.PhotoImage(Image.open(path).resize((29, 29), Image.LANCZOS))
    reload_button = Button(w, image=reload_img, command=lambda: createImage(1), relief="flat")
    reload_button.place(x=390, y=240)

    registerbtn = Button(w, text="Register", command=check_and_register, bg="#57a1f8", fg="white", cursor="hand2")
    registerbtn.config(padx=80)
    registerbtn.place(x=150, y=400)

    w.bind('<Return>', lambda event: check_and_register())

    def raise_frame(frame):
        frame.tkraise()
    Button(l, text = 'Create new account', font=('Time New Roman',12), border=2,bg='#F5FFFA',fg='black', command=lambda:raise_frame(w)).place(x=80,y=350)   
    Button(w, text = 'Back to Login Page', font=('Time New Roman',12), border=2,bg='#F5FFFA',fg='black', command=lambda:raise_frame(l)).place(x=150,y=450)

    root1.mainloop()

if __name__ == "__main__":
    main1()