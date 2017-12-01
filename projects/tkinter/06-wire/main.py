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

starting_width = 800
starting_height = 600
print("Starting root window dimensions: {}x{}".format(starting_width,starting_height))

root.minsize(320, 240)
max_width = screen_width = int(screen_width * .99)
max_height = screen_height = int(screen_height * .95)
root.maxsize(max_width, max_height)

starting_x = int((screen_width / 2) - (starting_width / 2))
starting_y = int((screen_height / 2) - (starting_height / 2))

root.geometry("{}x{}+{}+{}".format(starting_width, starting_height, starting_x, starting_y))

gpfc = GraphPaperFramedCanvas(root)
gpfc.pack(fill="both", expand=True)

gate1 = AndGate(gpfc.canvas, 'AndGate', 100, 350)
gate2 = OrGate(gpfc.canvas, 'OrGate', 100, 100)
gate3 = XOrGate(gpfc.canvas, 'XOrGate', 300, 250)
gate4 = BufferGate(gpfc.canvas, 'Buffer', 500, 350)
gate5 = NotGate(gpfc.canvas, 'Inverter', 200, 500)

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

root.mainloop()

