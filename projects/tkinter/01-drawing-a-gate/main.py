#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gate import AndGate

grid_line_width = 1  # the grid really needs to be made into an object

root = Tk()

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
frame_top.grid(row=0, column=0)

frame = Frame(root, width=800, height=480)
frame.grid(row=1, column=0)
#canvas = Canvas(root, width=640, height=480, borderwidth=0, background="#eeffee", scrollregion=(0,0,640,480))
canvas = Canvas(frame, width=640, height=480, borderwidth=0, background="#eeffee", scrollregion=(0,0,1024,768))
#canvas.pack(expand=True, fill="both") # Canvas will be a fixed size

hbar = Scrollbar(frame, orient=HORIZONTAL)
hbar.pack(side=BOTTOM, fill=X)
hbar.config(command=canvas.xview)

vbar = Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand=True, fill="both")

my_1st_gate = AndGate(canvas, 'foo', 100, 50)
my_2nd_gate = AndGate(canvas, 'bar', 100, 150)
my_3rd_gate = AndGate(canvas, 'zoo', 100, 250)

def on_motion(event):
    x, y = event.x, event.y
    if x < 0: x = 0
    if y < 0: y = 0
    #print('{}, {}'.format(x, y))
    mouse_coords_var.set("x={}, y={}".format(x , y))

def on_zoom(event):
    x, y = event.x, event.y
    scale_factor = 1.0
    # print("Delta: {}  x{} y{}".format(str(event.delta),event.x,event.y))
    if (event.delta > 0):
        #canvas.scale("all", event.x, event.y, 1.1, 1.1)
        scale_factor = 1.1
    elif (event.delta < 0):
        #canvas.scale("all", event.x, event.y, 0.9, 0.9)
        scale_factor = 0.9

    # We scale relative to point (event.x, event.y) to simulate zooming in/out
    #my_1st_gate.scale(x, y, scale_factor)
    #my_2nd_gate.scale(x, y, scale_factor)
    #my_3rd_gate.scale(x, y, scale_factor)

    # Try scaling relative to center of canvas
    x = canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2
    my_1st_gate.scale(x, y, scale_factor)
    my_2nd_gate.scale(x, y, scale_factor)
    my_3rd_gate.scale(x, y, scale_factor)
    global grid_line_width
    grid_line_width = grid_line_width * scale_factor

    canvas.scale('grid_line', x, y, scale_factor, scale_factor)
    canvas.itemconfigure('grid_line', width=grid_line_width)


canvas.bind_all('<Motion>', on_motion)
canvas.bind_all('<MouseWheel>', on_zoom)


def scroll_start(event):
    #canvas.scan_mark(event.x, event.y)
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas_mouse_coords_var.set("x={}, y={}".format(x , y))



def scroll_move(event):
    #canvas.scan_dragto(event.x, event.y, gain=1)
    pass

def draw_grid(event):
    w = canvas.winfo_width()   # Get current width of canvas
    h = canvas.winfo_height()  # Get current height of canvas
    canvas.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines
    for i in range(0, w, 10):
        canvas.create_line([(i, 0), (i, h)], fill="#ddffdd", tag='grid_line')

    # Creates all horizontal lines
    for i in range(0, h, 10):
        canvas.create_line([(0, i), (w, i)], fill="#ddffdd", tag='grid_line')

    canvas.tag_lower('grid_line')
    canvas_size_var.set("width={}, height={}".format(w, h))


# This is what enables scrolling with the mouse:
canvas.bind("<Shift-ButtonPress-1>", scroll_start)
canvas.bind("<Shift-B1-Motion>", scroll_move)
canvas.bind("<Configure>", draw_grid)

root.mainloop()

