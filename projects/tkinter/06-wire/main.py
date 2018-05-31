#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gate import *
from wire import *
from canvas import GraphPaperFramedCanvas

root = Tk()

# Window Transparency
root.attributes("-alpha", 0.85)
#root.wm_attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen dimensions: {}x{}".format(screen_width,screen_height))

starting_window_width = 800
starting_window_height = 600
print("Starting root window dimensions: {}x{}".format(starting_window_width, starting_window_height))

root.minsize(320, 240)
max_width = screen_width = int(screen_width * .99)
max_height = screen_height = int(screen_height * .95)
root.maxsize(max_width, max_height)

starting_window_loc_x = int((screen_width / 2) - (starting_window_width / 2))
starting_window_loc_y = int((screen_height / 2) - (starting_window_height / 2))

root.geometry("{}x{}+{}+{}".format(starting_window_width, starting_window_height, starting_window_loc_x, starting_window_loc_y))

# The canvas size will change when we zoom in/out, but this
# will be the starting canvas size
starting_canvas_size_x = 10000
starting_canvas_size_y = 10000

gpfc = GraphPaperFramedCanvas(root, starting_canvas_size_x, starting_canvas_size_y)
gpfc.pack(fill="both", expand=True)

starting_canvas_center_x = starting_canvas_size_x / 2
starting_canvas_center_y = starting_canvas_size_y / 2

gate1 = AndGate(gpfc.canvas, 'AndGate', starting_canvas_center_x + 100, starting_canvas_center_y + 350)
gate2 = OrGate(gpfc.canvas, 'OrGate', starting_canvas_center_x + 100, starting_canvas_center_y + 100)
gate3 = XOrGate(gpfc.canvas, 'XOrGate', starting_canvas_center_x + 300, starting_canvas_center_y + 250)
gate4 = BufferGate(gpfc.canvas, 'Buffer', starting_canvas_center_x + 500, starting_canvas_center_y + 350)
gate5 = NotGate(gpfc.canvas, 'Inverter', starting_canvas_center_x + 200, starting_canvas_center_y + 500)

wire1 = Wire(gpfc.canvas, 'Wire1')
wire1.connect(gate1.output_connection['OUT_0'], gate5.input_connection['IN_0'])
wire1.update_state()

wire2 = Wire(gpfc.canvas, 'Wire2')
wire2.connect(gate5.output_connection['OUT_0'], gate3.input_connection['IN_1'])
wire2.update_state()

wire3 = Wire(gpfc.canvas, 'Wire3')
wire3.connect(gate3.output_connection['OUT_0'], gate4.input_connection['IN_0'])
wire3.update_state()

wire4 = Wire(gpfc.canvas, 'Wire4')
wire4.connect(gate2.output_connection['OUT_0'], gate3.input_connection['IN_0'])
wire4.update_state()

# Scroll the canvas to the center, as that's where we've drawn the initial test circuit
gpfc.canvas.xview_moveto(0.5)
gpfc.canvas.yview_moveto(0.5)

root.mainloop()

