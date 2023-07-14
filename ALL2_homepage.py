import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import webbrowser
import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import speech_recognition
from pygame import mixer
from tkinter import simpledialog
import random
import os
from datetime import datetime
import time
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ALL2 Homepage\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main3():
    root3 = Tk()
    root3.geometry("1200x720")
    root3.title("Prototype Homepage")
    root3.configure(bg = "#FFFFFF")
    canvas = Canvas(root3,bg = "#FFFFFF",height = 900,width =1500,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.pack(fill=tk.BOTH, expand=True)
    rect1 = canvas.create_rectangle(240,112,1920,1200,fill="#606060",outline="")
    rect2 = canvas.create_rectangle(0,110,240,1200,fill="#F2F2F2",outline="")
    rect3 = canvas.create_rectangle(0,0,1920,110,fill="#F2F2F2",outline="")
    #Border
    canvas.create_rectangle(-1.99981689453125,110.0,1920,112.0,fill="#646464",outline="")
    #Database
    db = sqlite3.connect('academyhelpdesk.sqlite')
    cursor = db.cursor()

    #Clock 
    def update_clock():
        current_time = time.strftime('%H:%M:%S')
        clock.config(text=current_time)
        clock.after(1000, update_clock)


    clock = tk.Label(canvas,text='Clock', font=('Noto Sans', 21), bg='#F2F2F2')
    canvas.create_window(926, 45, anchor="center", window=clock)
    update_clock()
    
    display_name = canvas.create_text(1060, 30, anchor="nw", text="User", fill="#000000", font=("Noto Sans", 20 * -1))

    #Scrollbars
    vscrollbar = ttk.Scrollbar(root3, orient=VERTICAL, command= canvas.yview)
    canvas.configure(yscrollcommand = vscrollbar.set)
    vscrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = NE)

    scrollbar2 = ttk.Scrollbar(root3, orient=HORIZONTAL, command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar2.set)
    scrollbar2.place(relx = 0, rely = 1, relwidth = 1, anchor = SW)

    canvas.configure(scrollregion=canvas.bbox("all"))

    #Mousewheel Scrolling
    canvas.bind('<MouseWheel>', lambda event:canvas.yview_scroll(-int(event.delta / 100), "units"))
    #Horizontal Mousewheel Scrolling
    canvas.bind('<Control MouseWheel>', lambda event:canvas.xview_scroll(-int(event.delta / 100), "units"))

    #PDF Viewer
    def view_pdf(file_path):
        try:
            webbrowser.open(file_path)
        except FileNotFoundError:
            messagebox.showerror("PDF Viewer", "File not found.")

    #Pop Up Modules
    def popup1():
        topup = tk.Toplevel()
        topup.title('Module Results')
        mbox = tk.Listbox(topup, height=10, width=50)
        mbox.pack()
        load_pdf_files2(mbox)

    def load_pdf_files2(listbox):
        folder_path1 = "D:\Documents\ProjectALL2\CA&N"
        pdf_files = [f for f in os.listdir(folder_path1) if f.endswith('.pdf')]
        for i, file in enumerate(pdf_files):
            file_path = os.path.join(folder_path1, file)
            listbox.insert(tk.END, file)
            listbox.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

    def popup2():
        topup = tk.Toplevel()
        topup.title('Module Results')
        mbox = tk.Listbox(topup, height=10, width=50)
        mbox.pack()
        load_pdf_files3(mbox)

    def load_pdf_files3(listbox):
        folder_path1 = "D:\Documents\ProjectALL2\Maths"
        pdf_files = [f for f in os.listdir(folder_path1) if f.endswith('.pdf')]
        for i, file in enumerate(pdf_files):
            file_path = os.path.join(folder_path1, file)
            listbox.insert(tk.END, file)
            listbox.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

    def popup3():
        topup = tk.Toplevel()
        topup.title('Module Results')
        mbox = tk.Listbox(topup, height=10, width=50)
        mbox.pack()
        load_pdf_files4(mbox)

    def load_pdf_files4(listbox):
        folder_path1 = "D:\Documents\ProjectALL2\OOP"
        pdf_files = [f for f in os.listdir(folder_path1) if f.endswith('.pdf')]
        for i, file in enumerate(pdf_files):
            file_path = os.path.join(folder_path1, file)
            listbox.insert(tk.END, file)
            listbox.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

    #Search Function
    keyin=StringVar()
    mixer.init()
    def search():
        fetch_query = sbar.get().lower()
        
        if sbar.get()!='':
            if keyin.get()=='google':
                webbrowser.open(f'https://www.google.com/search?q={sbar.get()}')
            elif keyin.get()=='edge':
                webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(f'https://www.google.com/search?q={sbar.get()}')
            elif keyin.get()=='youtube':
                webbrowser.open(f'https://www.youtube.com/results?search_query={sbar.get()}')
            elif keyin.get() == 'module':
                if '4004cem' in fetch_query:
                    popup1()
                elif '4068cem' in fetch_query:
                    popup2()
                elif '4003cem' in fetch_query:
                    popup3()
                else:
                    messagebox.showinfo('Try Again', "Please type in the subject code for the resources you're looking for. Example: 4004CEM")

        else:
            messagebox.showerror('Error',"No input detected")    

    #Voice Search    
    def voice():
        mixer.music.load('audioprompt.mp3')
        mixer.music.play()
        sr=speech_recognition.Recognizer()
        with speech_recognition.Microphone()as m:
            try:
                sr.adjust_for_ambient_noise(m, duration=0.2)
                audio=sr.listen(m)
                message = sr.recognize_google(audio)
                mixer.music.load('audioprompt.mp3')
                mixer.music.play()
                sbar.delete(0,END)
                sbar.insert(0,message)
                search()
            except:
                pass

    def enter_key(value):
        sButton.invoke()

    root3.bind('<Return>',enter_key)

    #Images
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))#Chatbot
    image_1 = canvas.create_image(39,444,image=image_image_1)
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))#Appointment
    image_2 = canvas.create_image(39,345,image=image_image_2)
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))#Discussions
    image_4 = canvas.create_image(39,245,image=image_image_4)
    image_image_5 = PhotoImage(file=relative_to_assets("image_3.png"))#Modules
    image_5 = canvas.create_image(39,144,image=image_image_5)
    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))#INTI Banner
    image_6 = canvas.create_image(150,45,image=image_image_6)
    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))#User Icon
    image_7 = canvas.create_image(1030,45,image=image_image_7)

    #Top Panel
    #Search Bar
    sbar=Entry(root3,width=39,font=("Noto Sans",14),bd=3)
    sbox = canvas.create_window(550,45,window=sbar)
    #Radio Buttons
    #Google
    ggrbutton=ttk.Radiobutton(root3,text='Google',value='google',variable=keyin)
    rbutton1 = canvas.create_window(360,79,window=ggrbutton)
    #Microsoft Edge
    edgrbutton=ttk.Radiobutton(root3,text='Edge',value='edge',variable=keyin)
    rbutton2 = canvas.create_window(480,79,window=edgrbutton)
    #Youtube
    ytrbutton=ttk.Radiobutton(root3,text='Youtube',value='youtube',variable=keyin)
    rbutton3 = canvas.create_window(600,79,window=ytrbutton)
    #Modules
    modulrbutton=ttk.Radiobutton(root3,text='Modules',value='module',variable=keyin)
    rbutton4 = canvas.create_window(720,79,window=modulrbutton)
    #Default Radio Button
    keyin.set('google')

    #Microphone Button
    btn_image2 = PhotoImage(file=relative_to_assets("button_2.png"))
    micButton = Button(image=btn_image2,borderwidth=0,highlightthickness=0,
                    command=voice,relief="flat")
    topbutton1 = canvas.create_window(780,45,window=micButton)

    #Search Button
    btn_image3 = PhotoImage(file=relative_to_assets("button_3.png"))
    sButton = Button(image=btn_image3,borderwidth=0,highlightthickness=0,
                    command=search,relief="flat")
    topbutton2 = canvas.create_window(820,45,window=sButton)

    #User Configuration Button
    def show_dropdown_menu():
        menu.tk_popup(uproButton.winfo_rootx(), uproButton.winfo_rooty() + uproButton.winfo_height())

    def change_background_color():
        color1 = simpledialog.askstring("Change Background Color", "Enter Color/Color Code for Main Panel:")
        color2 = simpledialog.askstring("Change Background Color", "Enter Color/Color Code for Side Panel:")
        color3 = simpledialog.askstring("Change Background Color", "Enter Color/Color Code for Top Panel:")
        if not color1:
            color1 = "#606060"
        if not color2:
            color2 = "#F2F2F2"
        if not color3:
            color3 = "#F2F2F2"
        canvas.itemconfig(rect1, fill=color1)
        canvas.itemconfig(rect2, fill=color2)
        canvas.itemconfig(rect3, fill=color3)

    menu = tk.Menu(root3, tearoff=False)
    menu.add_command(label="Change Background Color", command=change_background_color)

    btn_image4 = PhotoImage(file=relative_to_assets("button_4.png"))
    uproButton = Button(image=btn_image4,borderwidth=0,highlightthickness=0,
                    command=(show_dropdown_menu),relief="flat")
    topbutton3 = canvas.create_window(1130,45,window=uproButton)

    #Logout Button
    def logout(root3):
        root3.destroy()
        import ALL2_login
        ALL2_login.main1()

    lgoutButton = Button(root3,text="Logout",font=("Noto Sans",16),bg="red",fg="#FFFFFF",borderwidth=1,
                    command=lambda: logout(root3))
    topbutton4 = canvas.create_window(1290,45,window=lgoutButton)


    #Left Panel
    #Modules Button
    def module():
        root3.destroy()
        import ALL2_modules
        ALL2_modules.main4()

    moduleBTN = Button(root3,text="Modules",font=("Noto Sans",16),bg="#F2F2F2",borderwidth=0,command=(module))
    sidebutton1 = canvas.create_window(70,142,anchor=W,window=moduleBTN)

    #Discussion Button
    def discuss():
        root3.destroy()
        import ALL2_discussion
        ALL2_discussion.main5()
        
    discussBTN = Button(root3,text="Discussion",font=("Noto Sans",16),bg="#F2F2F2",borderwidth=0,command=(discuss))
    sidebutton2 = canvas.create_window(70,244,anchor=W,window=discussBTN)

    #Appointment Button
    def appointment():
        root3.destroy()
        import ALL2_appointments
        ALL2_appointments.main6()

    appointBTN = Button(root3,text="Appointments",font=("Noto Sans",16),bg="#F2F2F2",borderwidth=0,command=(appointment))
    sidebutton4 = canvas.create_window(70,344,anchor=W,window=appointBTN)

    #Chatbot Button
    def chatbot():
        import chatbot1
        chatbot1.main7()
    chatbotBTN = Button(root3,text="Chatbot",font=("Noto Sans",16),bg="#F2F2F2",borderwidth=0,command=(chatbot))
    sidebutton5 = canvas.create_window(70,443,anchor=W,window=chatbotBTN)

    #Recently Viewed Panel
    canvas.create_text(300,120,anchor="nw",text="Recently Viewed",fill="#F2F2F2",font=("Noto Sans", 27 * -1))
    #Panel
    class RecentlyViewed(tk.Frame):
        def __init__(self, master):
            super().__init__(master, bg="#F2F2F2", width=550, height=150)
            self.place(x=520, y=230, anchor="center")

            self.frame1 = tk.Frame(self, bg="#F2F2F2", width=550, height=150)
            self.frame2 = tk.Frame(self, bg="#F2F2F2", width=550, height=150)
            self.frame3 = tk.Frame(self, bg="#F2F2F2", width=550, height=150)
            self.frame4 = tk.Frame(self, bg="#F2F2F2", width=550, height=150)
            self.frame5 = tk.Frame(self, bg="#F2F2F2", width=550, height=150)
            self.frames = [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]

            message1 = tk.Message(self.frame1, width=350 , text="Test 1\nWelcome User",font=("Noto Sans", 20 * -1))
            message1.place(x=0, y=0)
            message2 = tk.Message(self.frame2, width=350 , text="Test 2\nEnjoy Your Stay",font=("Noto Sans", 20 * -1))
            message2.place(x=0, y=0)
            message3 = tk.Message(self.frame3, width=350 , text="Test 3\nRate 5 stars",font=("Noto Sans", 20 * -1))
            message3.place(x=0, y=0)
            message4 = tk.Message(self.frame4, width=350 , text="Test 4\nDon't forget to take a break",font=("Noto Sans", 20 * -1))
            message4.place(x=0, y=0)
            message5 = tk.Message(self.frame5, width=350 , text="Test 5\nHave a good day",font=("Noto Sans", 20 * -1))
            message5.place(x=0, y=0)

            for frame in self.frames:
                frame.place(x=0, y=0, relwidth=1, relheight=1)

            self.current_frame_index = 0
            self.hide_frames(0)

        def clear_frames(self):
            for frame in self.frames:
                for widget in frame.winfo_children():
                    widget.destroy()

        def hide_frames(self, index):
            for i, frame in enumerate(self.frames):
                if i == index:
                    frame.place(x=0, y=0, relwidth=1, relheight=1)
                else:
                    frame.place_forget()

        def next_frame(self):
            current_index = self.current_frame_index
            next_index = (current_index + 1) % len(self.frames)
            self.slide_to_left(self.frames[current_index], self.frames[next_index])
            self.current_frame_index = next_index
            self.hide_frames(next_index)

        def previous_frame(self):
            current_index = self.current_frame_index
            previous_index = (current_index - 1) % len(self.frames)
            self.slide_to_right(self.frames[current_index], self.frames[previous_index])
            self.current_frame_index = previous_index
            self.hide_frames(previous_index)

        def slide_to_left(self, current_frame, next_frame):
            x_current = 0
            x_next = 550
            for i in range(20):
                x_current -= 27.5
                x_next -= 27.5
                current_frame.place(x=x_current, y=0)
                next_frame.place(x=x_next, y=0)
                self.update_messages_position(next_frame)
                self.update()
                self.after(10)

        def slide_to_right(self, current_frame, previous_frame):
            x_current = 0
            x_previous = -550
            for i in range(20):
                x_current += 27.5
                x_previous += 27.5
                current_frame.place(x=x_current, y=0)
                previous_frame.place(x=x_previous, y=0)
                self.update_messages_position(previous_frame)
                self.update()
                self.after(10)


        def update_messages_position(self, frame):
            messages = frame.winfo_children()
            for message in messages:
                message.place_configure(x=0, y=0)

    rctview = RecentlyViewed(canvas)
    canvas.create_window(577, 240, anchor="center", window=rctview)

    # Next & Previous buttons For RECENTLY VIEWED PANEL
    btn_image5 = PhotoImage(file=relative_to_assets("button_5.png"))
    previousButton = Button(image=btn_image5,bg="#606060",borderwidth=0,highlightthickness=0,
                    command=rctview.previous_frame,relief="flat")
    previous = canvas.create_window(285,235,window=previousButton)

    btn_image6 = PhotoImage(file=relative_to_assets("button_6.png"))
    nextButton = Button(image=btn_image6,bg="#606060",borderwidth=0,highlightthickness=0,
                    command=rctview.next_frame,relief="flat")
    next = canvas.create_window(867,235,window=nextButton)

    #Topics of Interest Panel
    canvas.create_text(300,400,anchor="nw",text="Topics of Interest",fill="#F2F2F2",font=("Noto Sans", 27 * -1))
    #Topics
    toi_frame = tk.Frame(canvas, bg="#F2F2F2", width=550, height=550)
    topicslbl = Label(toi_frame, text="Topics:", font=("Noto Sans", 17 * -1))
    topicslbl.place(x=15,y=10)

    def load_pdf_files1():
        folder_path = "D:\Documents\ProjectALL2\Mix"
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

        # Shuffle the list of files randomly
        random.shuffle(pdf_files)
        
        # Display the first 5 files from the shuffled list
        for i, file in enumerate(pdf_files[:5]):
            file_path = os.path.join(folder_path, file)
            topics = tk.Label(toi_frame, text=file, font=("Noto Sans", 13 * -1), cursor='hand2')
            topics.place(x=30, y=50 + i * 30)  # Increment y coordinate for each label
            topics.bind('<Button-1>', lambda e, file_path=file_path: view_pdf(file_path))

    load_pdf_files1()
    
    #Discussions
    discussions = Label(toi_frame, text="Having doubts? Here are some active discussions that may help:", font=("Noto Sans", 17 * -1))
    discussions.place(x=15, y=250)

    cursor.execute("SELECT discussion_title FROM discussion_question")
    titles = cursor.fetchall()

    for i, title in enumerate(titles):
        label = Label(toi_frame, text=title[0], font=("Noto Sans", 13 * -1), cursor="hand2")
        label.place(x=30, y=300 + i * 30)
        label.bind("<Button-1>", lambda e, title=title[0]: discuss())


    canvas.create_window(577, 745, window=toi_frame)

    #Appointment Panel
    canvas.create_text(1017,116,anchor="nw",text="Pending Appointments",fill="#F2F2F2",font=("Noto Sans", 27 * -1))
    aptmt_frame = tk.Frame(canvas, bg="#F2F2F2", width=300, height=240)
    canvas.create_window(1170,283, window=aptmt_frame)
    appttl = Label(aptmt_frame, text="Title: Appointment 1", font=("Noto Sans", 19 * -1))
    appttl.place(x=15,y=10)
    appdt = Label(aptmt_frame, text="Date&Time: 7/3/23 3:00 pm", font=("Noto Sans", 19 * -1))
    appdt.place(x=15,y=40)
    applc = Label(aptmt_frame, text="Location: LR601", font=("Noto Sans", 19 * -1))
    applc.place(x=15,y=70)
    

    root3.mainloop()

if __name__ == "__main__":
    main3()