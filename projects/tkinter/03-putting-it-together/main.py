#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gate import AndGate
from canvas import GraphPaperFramedCanvas

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen dimensions: {}x{}".format(screen_width,screen_height))

root.minsize(320, 240)
root.maxsize(screen_width - 20, screen_height - 60)
root.attributes("-alpha", 0.85)

frame_top = Frame(root, width=800, height=100)
mouse_coords_var = StringVar()
mouse_coords_var.set("INIT")
mouse_coords_label = Label(frame_top, textvariable=mouse_coords_var)
mouse_coords_label.pack()

canvas_size_var = StringVar()
canvas_size_var.set("INIT")
canvas_size_label = Label(frame_top, textvariable=canvas_size_var)
canvas_size_label.pack()

canvas_mouse_coords_var = StringVar()
canvas_mouse_coords_var.set("INIT")
canvas_mouse_coords_label = Label(frame_top, textvariable=canvas_mouse_coords_var)
canvas_mouse_coords_label.pack()


gpfc = GraphPaperFramedCanvas(root)
gpfc.pack(fill="both", expand=True)

my_1st_gate = AndGate(gpfc.canvas, 'foo', 100, 50)
my_2nd_gate = AndGate(gpfc.canvas, 'bar', 100, 150)
my_3rd_gate = AndGate(gpfc.canvas, 'zoo', 100, 250)

root.mainloop()

