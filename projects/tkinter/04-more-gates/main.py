#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gate import *
from canvas import GraphPaperFramedCanvas

root = Tk()

# Window Transparency
root.attributes("-alpha", 0.75)
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

# Let's draw near the center of the 8000x8000 canvas
my_1st_gate = AndGate(gpfc.canvas, 'foo', 4000, 4050)
my_2nd_gate = AndGate(gpfc.canvas, 'bar', 4000, 4150)
my_3rd_gate = AndGate(gpfc.canvas, 'zoo', 100, 250)
my_4th_gate = OrGate(gpfc.canvas, 'or001', 100, 100)
my_5th_gate = XOrGate(gpfc.canvas, 'xor002', 100, 350)
my_6th_gate = BufferGate(gpfc.canvas, 'buf003', 300, 350)
my_7th_gate = NotGate(gpfc.canvas, 'not004', 300, 100)

root.mainloop()

