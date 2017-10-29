#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gate import AndGate

root = Tk()
w = Label(root, text="Hello, world!")
w.pack()

canvas = Canvas(root, width=1024, height=768, borderwidth=0, background="skyblue")
canvas.pack(expand=True, fill="both")

my_1st_gate = AndGate(canvas, 'foo', 100, 50)
my_2nd_gate = AndGate(canvas, 'bar', 100, 150)
my_3rd_gate = AndGate(canvas, 'zoo', 100, 250)


def on_zoom(event):
    scale_factor = 1.0
    # print("Delta: {}  x{} y{}".format(str(event.delta),event.x,event.y))
    scale_factor = scale_factor + (event.delta * 0.1)
    # We scale relative to point (event.x, event.y) to simulate zooming in/out
    my_1st_gate.scale(event.x, event.y, scale_factor)
    my_2nd_gate.scale(event.x, event.y, scale_factor)
    my_3rd_gate.scale(event.x, event.y, scale_factor)


canvas.bind_all('<MouseWheel>', on_zoom)

root.mainloop()

