#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
import random # used to generate some random-sized rectangles


'''draw a grid pattern that looks like "Engineer's Graph Paper" on a canvas'''

class GraphPaperFramedCanvas(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.canvas_width = 8000
        self.canvas_height = 8000
        self.canvas = Canvas(self, width=self.canvas_width, height=self.canvas_height,
                                   borderwidth=0, highlightthickness=0)
        self.tag = "graph_paper"
        self.bg_color = "#eeffee"

        # First lets draw a background rectangle which we can tag
        # This will give us the ability to scroll the canvas only when clicking+dragging on the background
        # But will not drag when we click on an object on the canvas, as we want to be able to drag around
        # individual objects as well
        self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height,
                                           fill=self.bg_color, outline=self.bg_color, tag=self.tag)

        # Creates all vertical lines
        for i in range(0, self.canvas_width, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.canvas.create_line([(i, 0), (i, self.canvas_height)], fill=line_color, tag=self.tag)

        # Creates all horizontal lines
        for i in range(0, self.canvas_height, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.canvas.create_line([(0, i), (self.canvas_width, i)], fill=line_color, tag=self.tag)

        self.canvas.tag_lower(self.tag)

        self.xsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.ysb.set)
        self.canvas.config(xscrollcommand=self.xsb.set)
        self.canvas.config(scrollregion=self.canvas.bbox(self.tag))
        self.canvas.config(xscrollincrement=5, yscrollincrement=5)

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas.tag_bind(self.tag, "<ButtonPress-1>", self.scroll_start)
        self.canvas.tag_bind(self.tag, "<B1-Motion>", self.scroll_move)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Control-MouseWheel>", self.on_zoom)

    # Setup Click-and-Drag to pan the canvas

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    # Setup Two-Finger Swipe Gestures (Apple Magic Trackpad) to pan the canvas

    def on_mousewheel(self, event):
        # On the Trackpad Horizontal_Swipe looks like SHIFT + Vertical_Swipe
        shift = (event.state & 0x1) != 0
        if shift:
            self.canvas.xview_scroll(-1 * event.delta, "units")
        else:
            self.canvas.yview_scroll(-1 * event.delta, "units")

    def on_zoom(self, event):
        sf = 1.0
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        print("canvas size = {}x{}".format(w,h))
        x0 = self.canvas.bbox(self.tag)[0]
        y0 = self.canvas.bbox(self.tag)[1]
        x1 = self.canvas.bbox(self.tag)[2]
        y1 = self.canvas.bbox(self.tag)[3]
        print("bbox size = {}".format(self.canvas.bbox(self.tag)))
        print("x0 - x1 = {}".format(x1 - x0))
        print("y0 - y1 = {}".format(y1 - y0))
        # Zoom In
        if (event.delta > 0) and ((y1 - y0)  <= 10000):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
            sf = 1.1
        # Zoom Out
        elif (event.delta < 0) and ((x1 - x0) - 1000 >= w):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
            sf = 0.9

        # scale the size of canvas items to simulate zooming
        self.canvas.configure(scrollregion = self.canvas.bbox(self.tag))

        # Scale the line width on all canvas items too
        current_width = self.canvas.itemcget(self.tag, "width")
        new_width = float(current_width) * sf
        print("Current width = {}   -->  New width = {}".format(current_width, new_width))
        new_activewidth = new_width * 1.5  # the multiplier is how much magnification do we want over the line width
        # the item itself will remember its width, rather than an additional instance var
        self.canvas.itemconfigure(self.tag, width=new_width, activewidth=new_activewidth)






if __name__ == "__main__":
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print("Screen dimensions: {}x{}".format(screen_width,screen_height))

    root.minsize(320, 240)
    root.maxsize(screen_width - 20, screen_height - 60)
    root.attributes("-alpha", 0.95)

    my_frame = GraphPaperFramedCanvas(root)
    my_frame.pack(fill="both", expand=True)


    # draw a bunch of rectangles on our GraphPaperFramedCanvas
    for n in range(500):
        x0 = random.randint(0, my_frame.canvas_width - 200)
        y0 = random.randint(0, my_frame.canvas_height - 200)
        x1 = x0 + random.randint(50, 200)
        y1 = y0 + random.randint(50, 200)
        color = ("red", "orange", "yellow", "green", "blue")[random.randint(0,4)]
        my_frame.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill=color, activeoutline="green", tags=('graph_paper'))




    root.mainloop()



