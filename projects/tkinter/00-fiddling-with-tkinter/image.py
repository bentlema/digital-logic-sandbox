#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()

backgroundImage = PhotoImage(file="dog.gif")
label = Label(image=backgroundImage)
label.image = backgroundImage  # keep a reference to prevent it from being GC'ed!
#label.pack()

canvas = Canvas(root, width = 640, height = 480, background = 'gray')
canvas.create_image(50, 50, image=backgroundImage, tags="bg")
canvas.pack()

root.mainloop()

