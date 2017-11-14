import math
from tkinter import *

class Gate:
    """The parent class for all Gates"""

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
        self.tags = []
        self.tags.append(name_tag)

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


class AndGate(Gate):
    """The AND Gate draws itself on a canvas"""

    def __init__(self, canvas, name_tag, initial_x, initial_y):
        super().__init__(canvas, name_tag, initial_x, initial_y)

        x = self.x
        y = self.y

        points = []
        points.extend((x, y))  # first point in polygon
        points.extend((x + 29, y))

        # scale the unit circle by 30, as that's the distance from the center of the circle to the arc
        # See Also: https://en.wikipedia.org/wiki/Unit_circle
        for angle in range(-90, 90):
            arc_x = (math.cos(math.radians(angle)) * 30) + (x + 29)
            arc_y = (math.sin(math.radians(angle)) * 30) + (y + 30)
            points.extend((arc_x, arc_y))
            # print("{},{}".format(arc_x,arc_y))

        points.extend((x, y + 60))  # last point in polygon, which connects back to the 1st point

        self.perimeter = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.perimeter)


class OrGate(Gate):
    """The OR Gate draws itself on a canvas"""

    def __init__(self, canvas, name_tag, initial_x, initial_y):
        super().__init__(canvas, name_tag, initial_x, initial_y)

        x = self.x
        y = self.y

        points = []
        points.extend((x, y))  # first point in polygon

        # scale the unit circle by 30, as that's the distance from the center of the circle to the arc
        # See Also: https://en.wikipedia.org/wiki/Unit_circle
        for angle in range(-90, 90):
            arc_x = (math.cos(math.radians(angle)) * 65) + x
            arc_y = (math.sin(math.radians(angle)) * 30) + (y + 30)
            points.extend((arc_x, arc_y))

        for angle in range(90, 270):
            arc_x = (math.cos(math.radians(angle)) * -8) + x
            arc_y = (math.sin(math.radians(angle)) * 30) + (y + 30)
            points.extend((arc_x, arc_y))

        self.perimeter = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.perimeter)



