#!/usr/bin/env python3

from tkinter import *

def onObjectClick(event):
    print('Got object click', event.x, event.y)
    print('Closest Obj ID: {}'.format(event.widget.find_closest(event.x, event.y)))

def on_motion(event):
    x, y = event.x, event.y
    if x < 0: x = 0
    if y < 0: y = 0
    #print('{}, {}'.format(x, y))
    mouse_coords_var.set("x={}, y={}".format(x , y))

root = Tk()

mouse_coords_var = StringVar()
mouse_coords_var.set("INIT")
mouse_coords_label = Label(root, textvariable=mouse_coords_var)
mouse_coords_label.pack()

canvas = Canvas(root, width=400, height=400, borderwidth=5, background="skyblue")
obj1Id = canvas.create_line(0, 30, 100, 30, width=10, tags="obj1Tag")
obj2Id = canvas.create_text(50, 70, text='Click Me', tags='obj2Tag')

canvas.bind('<Motion>', on_motion)
canvas.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)

print('obj1Id: ', obj1Id)
print('obj2Id: ', obj2Id)
canvas.pack()
root.mainloop()
