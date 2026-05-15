# Pygame Window:

from tkinter import *

display = Tk()
display.title("My Tkinter Window")

display.geometry("400x400")
lbl = Label(display, text="Hello World!", fg="black", bg="white")
lbl.pack()
display.mainloop()