#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *


class GraphPaper():

    '''draw a grid on a canvas'''

    def __init__(self, canvas):
        self.c = canvas                           # Remember the canvas we are drawn on
        self.c_width = self.c.winfo_reqwidth()    # Get requested width of canvas
        self.c_height = self.c.winfo_reqheight()  # Get requested height of canvas
        self.tag = "grid_line"                    # All lines drawn will be tagged

        print("Canvas on which I will be drawn on is {}x{} in size.".format(self.c_width, self.c_height))

        # Creates all vertical lines
        for i in range(0, self.c_width, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.c.create_line([(i, 0), (i, self.c_height)], fill=line_color, tag='grid_line')

        # Creates all horizontal lines
        for i in range(0, self.c_height, 10):
            if (i % 100) == 0:
                line_color="#aaffaa"
            else:
                line_color="#ccffcc"
            self.c.create_line([(0, i), (self.c_width, i)], fill=line_color, tag='grid_line')

        canvas.tag_lower('grid_line')
        #canvas_size_var.set("width={}, height={}".format(w, h))



root = Tk()

# prevent resizing of root window
#root.minsize(640, 480)
#root.maxsize(1024, 768)
root.attributes("-alpha", 0.75)

frame = Frame(root, width=800, height=600)
frame.grid(row=0, column=0)

# Let's create a very large canvas, and then setup a "view portal" to view a part of it
#canvas = Canvas(root, width=8000, height=6000, borderwidth=0, background="#eeffee") #, confine=True, scrollregion=(0,0,800,600))

# Need to understand what exactly scrollregion does / allows?
# Need to write a ViewPortIfiedCanvas that keeps track of the ViewPort on a large canvas
# I want to, at minimum, pan around, but would be extra cool to be able to zoom in/out too
# Need to make sure, in both cases, that the viewport never extends beyond the edge of the canvas (if that's even possible)

canvas = Canvas(frame, width=8000, height=6000, borderwidth=0, background="#eeffee")
gp = GraphPaper(canvas)

vbar = Scrollbar(frame, orient=VERTICAL)
#vbar.pack(side=RIGHT, fill=Y)
vbar.grid(row=0, column=1, sticky=N+S)
vbar.config(command=canvas.yview)

hbar = Scrollbar(frame, orient=HORIZONTAL)
#hbar.pack(side=BOTTOM, fill=Y, expand=True)
hbar.grid(row=1, column=0, sticky=W+E)
hbar.config(command=canvas.xview)

canvas.config(yscrollcommand=vbar.set)
canvas.config(xscrollcommand=hbar.set)

#canvas.pack(side="top", fill="both", expand=True)
canvas.grid(row=0, column=0)
canvas.configure(width=800, height=600, scrollregion=(0, 0, 8000, 6000))


#canvas = Canvas(root, width=8000, height=6000, borderwidth=0, background="#eeffee", scrollregion=(-4000,-3000,4000,3000))
#canvas.pack(side="top", expand=True, fill="both", padx=0, pady=0, ipadx=0, ipady=0)


canvas.create_rectangle(1,1,21,21, fill="blue", outline="black")
canvas.create_rectangle(750,550,770,570, fill="red", outline="black")
canvas.create_rectangle(7980,5980,7999,5999, fill="red", outline="black")

#canvas.xview_scroll(800, "units")
#canvas.yview_scroll(600, "units")


root.mainloop()








