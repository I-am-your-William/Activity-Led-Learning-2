from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date

def main6():
    class Appointment:
        def __init__(self, master):
            self.master = master
            self.master.geometry("1300x700")
            self.master.resizable(False, False)

            self.left = Frame(self.master, width=800, height=720)
            self.left.pack(side=LEFT)

            self.right = Frame(self.master, width=600, height=720)
            self.right.pack(side=RIGHT)

            label = Label(self.left, text="4004CEM Computer Architecture and Networks" + "\n Vaithegy Doraisamy" , font=('Times New Roman', '15',' bold'), fg='black' )
            label.grid(row=0, column=0, padx=10, pady=10)

            btn = Button(self.left, text="Book Appointment", font=('Times New Roman', '15',' bold'), fg='black', command=self.open_appointment_popup)
            btn.grid(row=1, column=0, padx=10, pady=10)

            rHbtn = Button(self.left, text="Return Home", font=('Times New Roman', '15',' bold'), fg='black', command=self.returnH)
            rHbtn.grid(row=2, column=0, padx=10, pady=10)

            self.logs = Label(self.right, text="Appointment Comfirm With Vaithegy Doraisamy", font=('Times New Roman', '15',' bold'), fg='black')
            self.logs.place(x=100, y=100)

            self.box = Text(self.right, width=70, height=20)
            self.box.place(x=10, y=200)
            self.box.insert(END,"Hello"+ " \n")

            btn1=Button(self.right, text="View Appointment", font=('Times New Roman', '15',' bold'), fg='black', command=self.view_appointment)
            btn1.place(x=200, y=150)
        
        def returnH(self):
            root5.destroy()
            import ALL2_homepage
            ALL2_homepage.main3()
        
        def view_appointment(self):
            
            popup_window1 = Toplevel(self.master)
            popup_window1.title("Appointment")
            popup_window1.geometry("1300x700")

            view_appointmentframe = Frame(popup_window1, width=1300, height=700, bg="#F8F8F8")
            view_appointmentframe.place(x=0, y=0)

            view_appointmenttitle = Label(view_appointmentframe, text="Appointment", fg="Hotpink2", bg="#F8F8F8",
                                        font=("Time New Roman", 26, "bold")).place(x=550, y=100)

            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=20, fieldbackground="#F8F8F8")
            style.map("Treeview", bg=[('selected', "#F9ECE4")])

            thetreeframe = Frame(view_appointmentframe)
            thetreeframe.pack(padx=200, pady=250)

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

            displayrecord = cursor.execute("""SELECT Username, Appointment, Time, Date, Venue, PhoneNumber FROM (SELECT u.Username, a.Appointment,a.Date, a.Time, a.Venue, a.PhoneNumber
                                FROM appointment AS a JOIN user AS u
                                ON u.Username = a.Username) WHERE Username=?""", (self.selected_username.get(),))

            global count 
            count = 0
            for all in displayrecord: 
                if count % 2 == 0:  
                    manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('even',))
                else:
                    manage_tree.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3], all[4], all[5]), tags=('odd',))
                count += 1
            
        

            
            

        def open_appointment_popup(self):
            popup_window = Toplevel(self.master)
            popup_window.title("Appointment Booking")
            self.selected_username = StringVar()

            self.labeltitle = Label(popup_window,text="Appointment Booking for Vaithegy Doraisamy", font=('Times New Roman', '15',' bold'), fg='black')
            self.labeltitle.grid(row=0, column=0, padx=10, pady=10)

            self.username_label = Label(popup_window, text="Username", font=('Times New Roman', '15',' bold'), fg='black')
            self.username_label.grid(row=1, column=0, padx=10, pady=10)
            self.cmbo = ttk.Combobox(popup_window, values=self.get_usernames(), width=30, textvariable=self.selected_username)
            self.cmbo.grid(row=1, column=1, padx=10, pady=10)

            # Appointment
            self.appointment_label = Label(popup_window, text="Appointment", font=('Times New Roman', '15',' bold'), fg='black')
            self.appointment_label.grid(row=2, column=0, padx=10, pady=10)
            self.appointment_text = Entry(popup_window, width=30)
            self.appointment_text.grid(row=2, column=1, padx=10, pady=10)

            # Time
            self.time_label = Label(popup_window, text="Time", font=('Times New Roman', '15',' bold'), fg='black')
            self.time_label.grid(row=3, column=0, padx=10, pady=10)
            self.time_text = Entry(popup_window, width=30)
            self.time_text.grid(row=3, column=1, padx=10, pady=10)

            # Date
            self.date_label = Label(popup_window, text="Date", font=('Times New Roman', '15',' bold'), fg='black')
            self.date_label.grid(row=4, column=0, padx=10, pady=10)
            self.date_entry = DateEntry(popup_window, width=30, mindate=date.today())
            self.date_entry.grid(row=4, column=1, padx=10, pady=10)

            # Venue
            self.venue_label = Label(popup_window, text="Venue", font=('Times New Roman', '15',' bold'), fg='black')
            self.venue_label.grid(row=5, column=0, padx=10, pady=10)
            self.venue_text = Entry(popup_window, width=30)
            self.venue_text.grid(row=5, column=1, padx=10, pady=10)

            # Phone Number
            self.phone_label = Label(popup_window, text="Phone Number", font=('Times New Roman', '15',' bold'), fg='black')
            self.phone_label.grid(row=6, column=0, padx=10, pady=10)
            self.phone_text = Entry(popup_window, width=30)
            self.phone_text.grid(row=6, column=1, padx=10, pady=10)

            submit_btn = Button(popup_window, text="Confirm Appointment", width=20, height=2, bg='white',
                                command=self.add_appointment)
            submit_btn.grid(row=7,column=1, padx=10, pady=10)

        def get_usernames(self):
            dbcon = sqlite3.connect('academyhelpdesk.sqlite')
            cursor = dbcon.cursor()
            cursor.execute('SELECT Username FROM user')
            data = [row[0] for row in cursor.fetchall()]
            dbcon.close()
            return data

        def add_appointment(self):
            value1 = self.selected_username.get()
            value2 = self.appointment_text.get()
            value3 = self.time_text.get()
            value4 = self.date_entry.get()
            value5 = self.venue_text.get()
            value6 = self.phone_text.get()

            if value1 == '' or value2 == '' or value3 == '' or value4 == '' or value5 == '' or value6 == '':
                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                db = sqlite3.connect('academyhelpdesk.sqlite')
                cursor = db.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS appointment(
                                    Username VARCHAR NOT NULL,
                                    Appointment VARCHAR(100) NOT NULL,
                                    Time VARCHAR(20) NOT NULL,
                                    Date VARCHAR(20) NOT NULL,
                                    Venue VARCHAR(100) NOT NULL,
                                    PhoneNumber VARCHAR(20) NOT NULL
                                )""")
                cursor.execute("INSERT INTO appointment(Username, Appointment, Time, Date, Venue, PhoneNumber) VALUES(?,?,?,?,?,?)",
                            (value1, value2, value3, value4, value5, value6))
                db.commit()
                db.close()

                tkinter.messagebox.showinfo("Success", f"Appointment for {value1} has been comfirmed")
                self.box.insert(END, 'Booking fixed for ' +
                                str(value1) + ' at ' + str(value3) + '\n')

    root5 = Tk()
    Appointment(root5)
    root5.mainloop()

    
    
    

if __name__ == "__main__":
    main6()
