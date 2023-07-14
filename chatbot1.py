from tkinter import *
import webbrowser
import subprocess

def main7():
    global e
    root7 = Tk()
    root7.title("Chatbot")

    BG_GRAY = "#E51E1E"
    BG_COLOR = "#F2F2F2"
    TEXT_COLOR = "#000000"
    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"


    # Stationary items
    stationary_items = {
        "pencil case": "Pencil cases are available for exchange.",
        "pen": "Pens are available for exchange.",
        "eraser": "Erasers are available for exchange.",
        "correction tape": "Correction tape is available for exchange.",
    }

    # Send function
    def send():
        user_input = e.get().lower()
        send_message("You: " + user_input)
        process_user_input(user_input)
        e.delete(0, END)

    # Process user input and generate responses
    def process_user_input(user_input):
        if "hi" in user_input:
            send_message("Bot: Hi there, how can I help?")
        elif "modules" in user_input:
            root7.destroy()
            subprocess.run(["python", "ALL2_modules.py"])
        elif user_input in ["how are you", "how are you?"]:
            send_message("CloseAi: I'm fine! How about you?")
        elif user_input in ["fine", "good", "great"]:
            send_message("CloseAi: Great! How can I assist you?")
        elif "thank" in user_input:
            send_message("CloseAi: You're welcome! What else can I help you with?")
        elif "help" in user_input:
            send_message("CloseAi: Don't worry, I'm here to assist you. So what seems to be the issue?")
        elif user_input in ["technical", "admin"]:
                send_message("CloseAi: Here is a way to reach out to the admins for help")
                webbrowser.open("https://forms.gle/rNV5YhFXiFHT88R87")
        elif user_input in ["search", "materials", "resources"]:
                send_message("CloseAi: Please use the search bar to search for the materials you need")
                send_message("CloseAi: If you can't find the requested materials in the modules page, try searching through the web\
                             \n as the resources we provide are limited. Stay tuned for more updates in the future!")
        elif user_input in ["joke", "funny"]:
            send_message("CloseAi: Why don't skeletons fight each other?")
            send_message("CloseAi: Because they don't have the guts!")
        elif user_input in ["goodbye", "see you later", "see ya"]:
            send_message("CloseAi: Have a nice day!")
        elif user_input in ["appointments", "appointment"]:
            send_message("CloseAi: 1. Click on the appointment page.")
            send_message("CloseAi: 2. Select your username and fill in the remaining blank spaces")
            send_message("CloseAi: 3. Click on the 'Book Appointment' button and you're all set.")
        elif user_input in ["goodbye", "bye", "welcome"]:
            send_message("CloseAi: Thank you. Have a nice day!")
        elif any(keyword in user_input for keyword in ["bored", "fun", "games"]):
            send_message("CloseAi: How about a game of Tetris?")
        elif any(response_keyword in user_input for response_keyword in ["sure", "yes", "absolutely", "ya"]):
                subprocess.run(["python", "Tetris.py"])
                return  # Exit the function after launching the game
        elif user_input =="":
                send_message("CloseAi: How about you take a break and do whatever you like? Taking breaks are important, so don't stress yourself.")


        elif user_input in ["points","score"]:
            send_message("CloseAi: You can exchange the following items: stationary / pass year paper")
        elif user_input == "stationary":
            send_message("CloseAi: We have the following stationary items available:")
            for item in stationary_items:
                send_message("- " + item)
        elif "pass year" in user_input:
            webbrowser.open("https://www.cl.cam.ac.uk/teaching/exams/pastpapers/y2023p5q1.pdf")
            send_message("CloseAi: Here is a link to past year papers.")
        else:
            send_message("CloseAi: Sorry, I didn't understand that.")

    # Display messages in the chat window
    def send_message(message):
        txt.insert(END, "\n" + message)

    # Set up the GUI components
    label1 = Label(root7, bg=BG_COLOR, fg=TEXT_COLOR, text="CloseAi", font=FONT_BOLD, pady=10, width=20, height=1)
    label1.grid(row=0)

    txt = Text(root7, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    e = Entry(root7, bg="#F2F2F2", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)


    send_button = Button(root7, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
    send_button.grid(row=2, column=1)

    root7.bind('<Return>', lambda event: send())

    root7.mainloop()

if __name__ == "__main__":
    main7()
