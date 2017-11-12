import math
from tkinter import *

"""Eventually we need to separate out the common bits into a general Gate() object
    and then inherit from the general Gate() object for AndGate, OrGate, etc. """


class AndGate:
    """The AND Gate draws itself on a canvas"""

    def __init__(self, canvas, name_tag, initial_x, initial_y):
        """ pass in the canvas object id so we know where to draw our gate"""
        self.x = initial_x
        self.y = initial_y
        self.canvas = canvas  # remember the canvas that I'm drawn on

        # my primary name tag
        self.tag = name_tag
        # List of strings, each string is a name tag which is used to identify
        # groups of canvas items. One or more tags can be used to identify groups
        # of items that make up a larger compound item.  A primary tag name will
        # be passed in upon create, but multiple name tags can be added later via
        # add_tag method.  Eventually I will generate a random name tag using the
        # current time plus a random hash, so we can create many objects with
        # unique tag names, and dont have to worry about what the tag name is
        # outside of the object, or could make the arg optional so it works
        # either way
        self.tags = ["testing", "again"]
        self.tags.append(name_tag)

        x = self.x  # just so the following cancas.create's are easier to read
        y = self.y

        '''
        canvas.create_arc(x, y, x+54, y+50, start=-90, extent=180, width=2,
                          fill="blue", activefill="red", style=ARC, tags=name_tag)

        canvas.create_arc(x, y-4, x+58, y+54, start=-90, extent=180, width=2,
                          fill="blue", activefill="red", style=ARC, tags=name_tag)

        canvas.create_line(x+28, y, x, y, x, y+50, x+28, y+50, width=2,
                           fill="black", tags=name_tag)

        canvas.create_line(x+30, y-4, x-4, y-4, x-4, y+54, x+30, y+54, width=2,
                           fill="black", tags=name_tag)
        '''

        points = []
        points.extend((x-5, y-5))  # first point in polygon
        points.extend((x+29, y-5))

        # scale the unit circle by 30, as that's the distance from the center of the circle to the arc
        # See Also: https://en.wikipedia.org/wiki/Unit_circle
        for angle in range(-90, 90):
            arc_x = (math.cos(math.radians(angle)) * 30) + (x+29)
            arc_y = (math.sin(math.radians(angle)) * 30) + (y+25)
            points.extend((arc_x, arc_y))
            # print("{},{}".format(arc_x,arc_y))

        points.extend((x-5, y+55))
        points.extend((x-5, y-5))
        self.perimeter = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.perimeter)

        # this data is used to keep track of a canvas object being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # add bindings for clicking, dragging and releasing over any object with the name_tag
        self.canvas.tag_bind(self.tag, "<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.tag, "<ButtonRelease-1>", self.on_button_release)
        self.canvas.tag_bind(self.tag, "<B1-Motion>", self.on_button_motion)

    def on_button_press(self, event):
        # Begining drag of an object
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_button_release(self, event):
        # End drag of an object
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_button_motion(self, event):
        # Handle dragging of an object
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        # self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # We want to move all sub-objects, not just the one we grabbed with .find_closest
        self.canvas.move(self.tag, delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def add_tag(self, tag):
        self.tags.append(tag)

    def current_tags(self):
        return self.tags

    def print_tags(self):
        for t in self.tags:
            print("{}".format(t))

    '''
    This isn't used anymore
    def scale(self, x, y, sf):
        current_width = self.canvas.itemcget(self.tag, "width")
        new_width = float(current_width) * float(sf)  # scale the width of the outline also
        new_activewidth = new_width * 1.5  # the multiplier is how much magnification do we want over the line width
        print("x,y={} width = {}, activewidth = {}, scale_facter = {}".format((x ,y), new_width, new_activewidth, sf))
        self.canvas.scale(self.tag, x, y, sf, sf)
        # the item itself will remember its width, rather than an additional instance var
        self.canvas.itemconfigure(self.tag, width=new_width, activewidth=new_activewidth)
    '''
