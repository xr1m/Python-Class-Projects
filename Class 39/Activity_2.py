# Getting started with widgets:

from tkinter import *
from datetime import date

window = Tk()
window.title("My First Tkinter App")
window.geometry("400x300")

# Label widget:

lbl = Label(window, text="Hello", fg="black")
lbl.pack()

name_lbl = Label(window, text="Enter your name:")
name_lbl.pack()

name_entry = Entry(window)
name_entry.pack()

def display_content():
    name = name_entry.get()
    today = date.today()
    global Message
    Message = "Welcome to my first application\nToday's date is: "
    greeting = "\nHello there. " + name + "!\n"
    text_box.insert(END, Message)
    text_box.insert(END, today)
    text_box.insert(END, greeting)

text_box = Text(window, height=3)
text_box.pack()

btn = Button(window, text="Submit", command=display_content, height=1, bg="White", fg="Black")
btn.pack()

window.mainloop()