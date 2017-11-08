#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
import random # used to generate some random-sized rectangles


class GraphPaper():

    '''draw a grid pattern that looks like "Engineer's Graph Paper" on a canvas'''

    def __init__(self, canvas):
        self.c = canvas                           # Remember the canvas we are drawn on
        self.c_width = self.c.winfo_reqwidth()    # Get requested width of canvas
        self.c_height = self.c.winfo_reqheight()  # Get requested height of canvas
        self.tag = "graph_paper"                  # All lines drawn will be tagged

        #print("Canvas on which I will be drawn on is {}x{} in size.".format(self.c_width, self.c_height))

        # First lets draw a background rectangle which we can tag
        # This will give us the ability to scroll the canvas only when clicking+dragging on the background
        self.c.create_rectangle(0, 0, self.c_width, self.c_height, fill="#eeffee", outline="#eeffee", tag=self.tag)

        # Creates all vertical lines
        for i in range(0, self.c_width, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.c.create_line([(i, 0), (i, self.c_height)], fill=line_color, tag=self.tag)

        # Creates all horizontal lines
        for i in range(0, self.c_height, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.c.create_line([(0, i), (self.c_width, i)], fill=line_color, tag=self.tag)

        canvas.tag_lower(self.tag)



root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen dimensions: {}x{}".format(screen_width,screen_height))

root.minsize(320, 240)
root.maxsize(screen_width-20, screen_height-60)
root.attributes("-alpha", 0.75)

frame = Frame(root, bg="blue")
frame.pack(fill=BOTH, expand=YES)

# Let's create a very large canvas, and then setup a "view portal" to view a part of it
#
# Need to understand what exactly scrollregion does / allows?
# Need to write a class "BetterCanvas" that keeps track of the ViewPort on a large canvas
#  * Pan/Scroll by Click+Drag on Canvas or with scroll wheel / TrackPad
#  * Zoom with Shift+ScrollWheel
#
# As Zooming in/out is simulated by scaling all objects on the canvas up/down, we need
# to ensure we arn't able to scroll over to the edge where the background image is
# no longer showing (in our case, the graph paper).  I think we can do this by dynamically
# updating the scroll region and using bbox on our background graph paper object.
# 

canvas = Canvas(frame, width=8000, height=6000, borderwidth=0, highlightthickness=0)
gp = GraphPaper(canvas)

vbar = Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y, expand=YES)
vbar.config(command=canvas.yview)

hbar = Scrollbar(frame, orient=HORIZONTAL)
hbar.pack(side=BOTTOM, fill=X, expand=YES)
hbar.config(command=canvas.xview)

canvas.config(yscrollcommand=vbar.set)
canvas.config(xscrollcommand=hbar.set)

canvas.pack(fill=BOTH, expand=YES)
#canvas.configure(width=800, height=600, scrollregion=(0, 0, 8000, 6000))
canvas.configure(scrollregion=canvas.bbox('graph_paper'))
canvas.configure(xscrollincrement=5, yscrollincrement=5)

# create a small box in top left corner, and bottom right corner
canvas.create_rectangle(1,1,21,21, fill="blue", outline="black")
canvas.create_rectangle(7980,5980,7999,5999, fill="red", outline="black")
# and create a bunch more randomly all over the canvas
for n in range(500):
    x0 = random.randint(0, 8000)
    y0 = random.randint(0, 6000)
    x1 = x0 + random.randint(50, 200)
    y1 = y0 + random.randint(50, 200)
    color = ("red", "orange", "yellow", "green", "blue")[random.randint(0,4)]
    canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill=color, activefill="black", tags=n)






# Setup Click-and-Drag to pan the canvas

def scroll_start(event):
    canvas.scan_mark(event.x, event.y)

def scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

# We tag the background graph_paper to avoid scrolling when we click and drag an object
canvas.tag_bind("graph_paper", "<ButtonPress-1>", scroll_start)
canvas.tag_bind("graph_paper", "<B1-Motion>", scroll_move)



# Setup Two-Finger Swipe Gestures (Apple Magic Trackpad) to pan the canvas

def on_mousewheel(event):
    # On the Trackpad Horizontal_Swipe looks like SHIFT + Vertical_Swipe
    shift = (event.state & 0x1) != 0
    if shift:
        canvas.xview_scroll(-1 * event.delta, "units")
    else:
        canvas.yview_scroll(-1 * event.delta, "units")

canvas.bind("<MouseWheel>", on_mousewheel)



root.mainloop()








