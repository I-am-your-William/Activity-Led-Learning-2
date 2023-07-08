from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from io import BytesIO
import io

def raise_frame(frame):
    frame.tkraise()

def main5():
    root5=Tk()
    root5.geometry('1300x700')

    nameinput=StringVar()
    subject = StringVar()
    discusstitle=StringVar()
    content=StringVar()
    img= None
    filename = None

    ##############################Upload Post###################################################
    def upload_image():
        global filename,img
        f_types=[('Png files','*.png'),('Jpg files','*.jpg')]
        filename=filedialog.askopenfilename(filetypes=f_types)
        if(filename):
            img=Image.open(filename)
            img = img.resize((190,220))
            img = ImageTk.PhotoImage(img)
            label=Label(add_discussion, image=img, width=190, height=220)
            label.place(x=800,y=150)

    def submit():
        content = content_entry.get("1.0", "end").strip()
        if nameinput.get() == '' or discusstitle.get() == '':
            messagebox.showerror("Error", "Please complete the required fields!")
        else:
            try:
                if filename:
                    with open(filename, 'rb') as fb:
                        image_data = fb.read()
                else:
                    image_data = None

                db = sqlite3.connect('academyhelpdesk.sqlite')
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS discussion_question (
                        question_code INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        subject_code TEXT NOT NULL,
                        discussion_title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        image BLOB
                    )
                """)
                cursor.execute(
                    "INSERT INTO discussion_question (username, subject_code, discussion_title, content, image) VALUES (?, ?, ?, ?, ?)",
                    (nameinput.get(), subject_entry.get(), discusstitle.get(), content, image_data)
                )
                db.commit()
                db.close()

                messagebox.showinfo("Info", "Your post is published successfully.")
            except:
                messagebox.showerror('Error', 'Post creation failed. Please try again.')



    ##############################View Post###################################################
    '''def viewpost(): 
        viewpost = Frame(root5, bg='#FCE1F3', width=1300, height=700)
        viewpost.place(x=0, y=0)

        Button(viewpost, width=8, pady=5, text="Back", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12), 
            command=lambda: raise_frame(discusspage)).place(x=1000, y=54)  

        forumtitle = Label(viewpost, text="Discussion Forum", fg="Hotpink2", bg="#FCE1F3", font=("Time New Roman", 26, "bold"))
        forumtitle.place(x=500, y=54)

        forum = Frame(viewpost, width=900, height=500)
        forum .place(x=30, y=120)
        mycanvas = Canvas( forum , bg="white", width=900, height=500)
        mycanvas.pack(side=LEFT)
        scrollbar = Scrollbar( forum , orient=VERTICAL, command=mycanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        mycanvas.configure(yscrollcommand=scrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        frameincanvas = Frame(mycanvas)
        mycanvas.create_window((0, 0), window=frameincanvas, anchor="nw")

        db = sqlite3.connect('academyhelpdesk.sqlite')
        cursor = db.cursor()
        posts = cursor.execute("SELECT * FROM discussion_question")

        
        i = 0
        images = []
        for discussion_question in posts:
            questionframe = Frame(frameincanvas, bg='#F8F8F8', width=900, height=500)
            questionframe.grid(row=i, column=1, padx=1, pady=3)
            username = Label(questionframe, border=0, text=str(discussion_question[1]),bg='#F8F8F8', font=("Time New Roman",16,"bold"))
            username.place(x=10, y=20)
            subjectcode = Label(questionframe, border=0, text="Subject Code:" + discussion_question[2], bg='#F8F8F8', font=("Time New Roman", 13))
            subjectcode.place(x=10, y=60)
            question = Label(questionframe, border=0, text="Question:" + discussion_question[3], bg='#F8F8F8', font=("Time New Roman", 13))
            question.place(x=10, y=100)
            content = Label(questionframe, border=0, text='Content:' + discussion_question[4], bg='#F8F8F8', font=("Time New Roman", 13))
            content.place(x=10, y=140)

            image_data = discussion_question[5]
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((220, 220))
                photo = ImageTk.PhotoImage(image)
                imagelabel = Label(questionframe, image=photo)
                imagelabel.image = photo
                imagelabel.place(x=10, y=200)
                images.append(photo)


            i += 1

            comment_button = Button(questionframe, text="Comment", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12),
                                    command=lambda post_id=discussion_question[0]: comment_post(post_id))

            comment_button.place(x=10, y=450)

            comment_forum = Frame(questionframe, width=300, height=300)
            comment_forum.place(x=500, y=10)
            comment_canvas = Canvas(comment_forum, bg="white", width=300, height=300)
            comment_canvas.pack(side=LEFT)
            comment_scrollbar = Scrollbar(comment_forum, orient=VERTICAL, command=comment_canvas.yview)
            comment_scrollbar.pack(side=RIGHT, fill=Y)
            comment_canvas.configure(yscrollcommand=comment_scrollbar.set)
            comment_canvas.bind('<Configure>', lambda e: comment_canvas.configure(scrollregion=comment_canvas.bbox('all')))
            comment_frame = Frame(comment_canvas)
            comment_canvas.create_window((0, 0), window=comment_frame, anchor="nw")



            
        
            cursor.execute("SELECT * FROM comments WHERE post_id=?", (discussion_question[0],))
            comments = cursor.fetchall()
            comment_frame = Frame(questionframe, bg='#F8F8F8')
            comment_frame.place(x=500, y=10)

            comment_t = Label(comment_frame, text= "Comment" , bg='#F8F8F8', font=("Time New Roman", 15))
            comment_t.pack(anchor=W)

            for comment in comments:
                comment1= Label(comment_frame, text= comment[1] +" : "+ comment[2] , bg='#F8F8F8', font=("Time New Roman", 12))
                comment1.pack(anchor=W)
            i += 1
            

        


        forum1 = Frame(viewpost, width=300, height=500)
        forum1 .place(x=950, y=120) 
        mycanvas1 = Canvas( forum1 , bg="white", width=300, height=500)
        mycanvas1.pack(side=RIGHT)
        scrollbar1 = Scrollbar( forum1 , orient=VERTICAL, command=mycanvas1.yview)
        scrollbar1.pack(side=RIGHT, fill=Y)
        mycanvas1.configure(yscrollcommand=scrollbar1.set)
        mycanvas1.bind('<Configure>', lambda e: mycanvas1.configure(scrollregion=mycanvas1.bbox('all')))


        frameincanvas1 = Frame(mycanvas1)
        mycanvas1.create_window((0, 0), window=frameincanvas1, anchor="nw")

        db = sqlite3.connect('academyhelpdesk.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM comments WHERE post_id=?", (discussion_question[0],))
        comments = cursor.fetchall()

        for comment in comments:
            comment_frame = Frame(frameincanvas1, bg='#F8F8F8')
            comment_frame.place(x=500, y=10)
            comment_t = Label(comment_frame, text= "Comment" , bg='#F8F8F8', font=("Time New Roman", 15))
            comment_t.pack(anchor=W)
            comment1= Label(comment_frame, text= comment[1] +" : "+ comment[2] , bg='#F8F8F8', font=("Time New Roman", 12))
            comment1.pack(anchor=W)

        i += 1
            


        db.close() '''   

    ##############################View Post###################################################
    def viewpost(): 
        viewpost = Frame(root5, bg='#FCE1F3', width=1300, height=700)
        viewpost.place(x=0, y=0)

        Button(viewpost, width=8, pady=5, text="Back", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12), 
            command=lambda: raise_frame(discusspage)).place(x=1000, y=54)  

        forumtitle = Label(viewpost, text="Discussion Forum", fg="Hotpink2", bg="#FCE1F3", font=("Time New Roman", 26, "bold"))
        forumtitle.place(x=500, y=54)

        forum = Frame(viewpost, width=1200, height=500)
        forum.place(x=30, y=120)
        mycanvas = Canvas(forum, bg="white", width=1200, height=500)
        mycanvas.pack(side=LEFT)
        scrollbar = Scrollbar(forum, orient=VERTICAL, command=mycanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        mycanvas.configure(yscrollcommand=scrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        frameincanvas = Frame(mycanvas)
        mycanvas.create_window((0, 0), window=frameincanvas, anchor="nw")

        db = sqlite3.connect('academyhelpdesk.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM discussion_question")
        posts = cursor.fetchall()

        i = 0
        images = []
        for post in posts:
            questionframe = Frame(frameincanvas, bg='#F8F8F8', width=1200, height=500)
            questionframe.grid(row=i, column=1, padx=1, pady=3)
            username = Label(questionframe, border=0, text=str(post[1]), bg='#F8F8F8', font=("Time New Roman", 16, "bold"))
            username.place(x=10, y=20)
            subjectcode = Label(questionframe, border=0, text="Subject Code:" + post[2], bg='#F8F8F8', font=("Time New Roman", 13))
            subjectcode.place(x=10, y=60)
            question = Label(questionframe, border=0, text="Question:" + post[3], bg='#F8F8F8', font=("Time New Roman", 13))
            question.place(x=10, y=100)
            content = Label(questionframe, border=0, text='Content:' + post[4], bg='#F8F8F8', font=("Time New Roman", 13))
            content.place(x=10, y=140)

            image_data = post[5]
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((220, 220))
                photo = ImageTk.PhotoImage(image)
                imagelabel = Label(questionframe, image=photo)
                imagelabel.image = photo
                imagelabel.place(x=10, y=200)
                images.append(photo)

            comment_frame = Frame(questionframe, bg='#F8F8F8')
            comment_frame.place(x=500, y=10)
            comment_t = Label(comment_frame, text="Comment", bg='#F8F8F8', font=("Time New Roman", 15))
            comment_t.pack(anchor=W)

            cursor.execute("SELECT * FROM comments WHERE post_id=?", (post[0],))
            comments = cursor.fetchall()

            for comment in comments:
                comment1 = Label(comment_frame, text=comment[1] + " : " + comment[2], bg='#F8F8F8', font=("Time New Roman", 12))
                comment1.pack(anchor=W)

            comment_button = Button(questionframe, text="Comment", bg="#F5FFFA", fg="black", border=0, font=("Time New Roman", 12),
                                    command=lambda post_id=post[0]: comment_post(post_id))
            comment_button.place(x=10, y=450)

            i += 1

        db.close()


    ###################################Write comment##########################################
    def comment_post(post_id):
        comment_window = Toplevel(root5)
        comment_window.geometry('500x500')
        comment_window.title('Comment')

        # Retrieve the post details based on the post_id
        db = sqlite3.connect('academyhelpdesk.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM discussion_question WHERE question_code=?", (post_id,))
        post_details = cursor.fetchone()
        db.close()

        # Display the post details in the comment window
        username_label = Label(comment_window, text="Username:", font=("Times New Roman", 12))
        username_label.pack()
        username_value = Label(comment_window, text=post_details[1], font=("Times New Roman", 12, "bold"))
        username_value.pack()

        subject_label = Label(comment_window, text="Subject Code:", font=("Times New Roman", 12))
        subject_label.pack()
        subject_value = Label(comment_window, text=post_details[2], font=("Times New Roman", 12, "bold"))
        subject_value.pack()

        question_label = Label(comment_window, text="Question:", font=("Times New Roman", 12))
        question_label.pack()
        question_value = Label(comment_window, text=post_details[3], font=("Times New Roman", 12, "bold"))
        question_value.pack()

        content_label = Label(comment_window, text="Content:", font=("Times New Roman", 12))
        content_label.pack()
        content_value = Label(comment_window, text=post_details[4], font=("Times New Roman", 12, "bold"))
        content_value.pack()

        # Add a text box for entering comments
        c_label = Label(comment_window, text="Username:", font=("Times New Roman", 12))
        c_label.pack()
        comment_user = Entry(comment_window, width=40,textvariable=nameinput)
        comment_user.pack()
        comment_label = Label(comment_window, text="Enter Comment:", font=("Times New Roman", 12))
        comment_label.pack()
        comment_text = Text(comment_window, height=5, width=40)
        comment_text.pack()

        def submit_comment():
            comment = comment_text.get("1.0", "end").strip()
            if comment:
                # Save the comment in the database
                db = sqlite3.connect('academyhelpdesk.sqlite')
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS comments (
                        post_id INTEGER FOIREIGN KEY,
                        username TEXT NOT NULL,
                        comment TEXT NOT NULL
                    )
                """)
                cursor.execute("INSERT INTO comments (post_id, username, comment) VALUES (?, ?, ?)",
                            (post_id, comment_user.get(), comment))
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Comment submitted successfully.")
                comment_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter a comment.")
        
        submit_button = Button(comment_window, text="Submit", bg="#F2EEED", fg="black", font=("Times New Roman", 12),
                                command=submit_comment)
        submit_button.pack()

        comment_window.mainloop()

    
    ###################################################Create Post Widget
    add_discussion = Frame(root5, width=1300, height=700, bg='#F2DBD5')
    add_discussion.place(x=0,y=0)
    addNew = Label(add_discussion, text='Create Post',bg='#F2DBD5',font=("Time New Roman",20,"bold")).place(x=550,y=50)

    username=Label(add_discussion, text = "Username :", bg='#F2DBD5', font = ("Times New Roman bold", 13)).place(x=200,y=150)
    subject=Label(add_discussion, text = "Select subject :", bg='#F2DBD5', font = ("Times New Roman bold", 13)).place(x=200,y=200)
    discusstitle_label = Label(add_discussion, text='Discussion Title:', bg='#F2DBD5', font=('Times New Roman bold', 13)).place(x=200,y=250)
    content_label = Label(add_discussion, text='Content:', bg='#F2DBD5', font=('Times New Roman bold', 13)).place(x=200,y=300)

    im = LabelFrame(add_discussion, bg='white', width=190, height=220).place(x=800,y=150)

    username_entry =Entry(add_discussion, width=40,textvariable=nameinput).place(x=400,y=150)
    subject_entry = ttk.Combobox(add_discussion, width = 37, textvariable = subject)
    subject_entry['values'] = ('4004CEM','4003CEM','4068CEM','4009CEM')
    subject_entry.place(x=400,y= 200)
    discusstitle_entry =Entry(add_discussion, width=40,textvariable=discusstitle).place(x=400,y=250)
    content_entry = Text(add_discussion, width=40)
    content_entry.place(x=400, y=300, height=100)

    Create_new=Button(add_discussion,text='Create New', bg="#F2EEED",fg="black",border=0,font=('Times New Roman bold', 13), command=submit).place(x=450,y=420)
    uploadImage_button=Button(add_discussion, text='Upload Image', bg="#F2EEED",fg="black",border=0,font=('Times New Roman bold', 13), command=upload_image).place(x=800,y=420)
    Button(add_discussion,  width=8,pady=5,text="Back",bg="#F2EEED",fg="black",border=0,font=("Time New Roman",12), command =lambda:raise_frame(discusspage)).place(x=900,y=50)

    ###########################################################Discussion forum widget
    discusspage=Frame(root5,width=1300,height=700, bg='#F2DBD5')
    discusspage.place(x=0,y=0)

    title=Label(discusspage,text = 'Discussion Forum ',font=("Time New Roman",30), bg='#F2DBD5')
    title.place(x=525,y=50)
    btn1=Button(discusspage,width=10,pady=5,text="Create Post",bg="#F2EEED",fg="black",border=10,font=("Time New Roman",12), command=lambda:raise_frame(add_discussion)).place(x=200,y=170)
    btn4=Button(discusspage,width=30,pady=5,text="Forum",bg="#F5FFFA",fg="black",border=0,font=("Time New Roman",12), command = lambda:viewpost()).place(x=520,y=170)
    
    #Home Button
    def returnH():
        root5.destroy()
        import ALL2_homepage
        ALL2_homepage.main3()

    rHButton = Button(discusspage,text="Return Home",font=("Noto Sans",15),bg="#F5FFFA",fg="black",borderwidth=1,
                    command=(returnH))
    rHButton.place(x=580,y=300)

    root5.mainloop()

if __name__ == "__main__":
    main5()