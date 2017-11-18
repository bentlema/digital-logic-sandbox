import math


class InputConnection:

    def __init__(self, parent, label):
        self.state = bool(False)
        self.label = label


class OutputConnection:

    def __init__(self, parent, starting_point, label):
        self.state = bool(False)
        self.label = label

        (x0, y0) = starting_point
        (x1, y1) = x0 + 10, y0

        self.output_line = parent.canvas.create_line(x0, y0, x1, y1, width=2, activewidth=2, fill="blue", activefill="blue", tag=parent.tag)
        parent.canvas.addtag_withtag("scale_on_zoom_2_2", self.output_line)

        self.output_joint = parent.canvas.create_oval(x1, y1 - 6, x1 + 12, y1 + 6, width=2, activewidth=5, fill="white", outline="blue", activeoutline="orange", tag=parent.tag)
        parent.canvas.addtag_withtag("scale_on_zoom_2_5", self.output_joint)


class InvertedOutputConnection:

    def __init__(self, parent, starting_point, label):
        self.state = bool(True)
        self.label = label

        (x0, y0) = starting_point
        (x1, y1) = x0 + 10, y0

        self.output_line = parent.canvas.create_line(x0 + 8, y0, x1 + 8, y1, width=2, activewidth=2, fill="blue", activefill="blue", tag=parent.tag)
        parent.canvas.addtag_withtag("scale_on_zoom_2_2", self.output_line)

        self.output_inverter = parent.canvas.create_oval(x0, y0 - 4, x0 + 8, y0 + 4, width=2, activewidth=5, fill="white", outline="blue", activeoutline="orange", tag=parent.tag)
        parent.canvas.addtag_withtag("scale_on_zoom_2_5", self.output_inverter)

        self.output_joint = parent.canvas.create_oval(x1 + 8, y1 - 6, x1 + 20, y1 + 6, width=2, activewidth=5, fill="white", outline="blue", activeoutline="orange", tag=parent.tag)
        parent.canvas.addtag_withtag("scale_on_zoom_2_5", self.output_joint)


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
        self.canvas.tag_bind(self.tag + "dragable", "<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.tag + "dragable", "<ButtonRelease-1>", self.on_button_release)
        self.canvas.tag_bind(self.tag + "dragable", "<B1-Motion>", self.on_button_motion)

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


class BufferGate(Gate):
    """The Buffer Gate draws itself on a canvas"""

    def __init__(self, canvas, name_tag, initial_x, initial_y):
        super().__init__(canvas, name_tag, initial_x, initial_y)

        x = self.x
        y = self.y

        points = []
        points.extend((x, y))  # first point in polygon
        points.extend((x + 58, y + 28))
        points.extend((x +  0, y + 56))

        self.perimeter = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.perimeter)
        self.canvas.addtag_withtag(self.tag + "dragable", self.perimeter)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # A Buffer gate has one input connection and one output connection
        self.input_connection['IN_0'] = InputConnection(self, 'Input 0')
        self.output_connection['OUT_0'] = OutputConnection(self, (x + 58, y + 28), 'Output')

        # Ensure initial value of output is correct
        self.update_state()

    def update_state(self):
        self.output_connection['OUT_0'].state = self.input_connection['IN_0'].state


class NotGate(Gate):
    def __init__(self, canvas, name_tag, initial_x, initial_y):
        super().__init__(canvas, name_tag, initial_x, initial_y)

        x = self.x
        y = self.y

        points = []
        points.extend((x, y))  # first point in polygon
        points.extend((x + 58, y + 28))
        points.extend((x +  0, y + 56))

        self.perimeter = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.perimeter)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # A Buffer gate has one input connection and one output connection
        self.input_connection['IN_0'] = InputConnection(self, 'Input 0')
        self.output_connection['OUT_0'] = InvertedOutputConnection(self, (x + 58, y + 28), 'Output')

        # Ensure initial value of output is correct
        self.update_state()

        # Tag those parts that we can click on and drag the gate
        self.canvas.addtag_withtag(self.tag + "dragable", self.perimeter)
        self.canvas.addtag_withtag(self.tag + "dragable", self.output_connection['OUT_0'].output_inverter)

        # Tag the specific canvas items we want to activate (highlight) together
        self.canvas.addtag_withtag(self.tag + "activate_together", self.perimeter)
        self.canvas.addtag_withtag(self.tag + "activate_together", self.output_connection['OUT_0'].output_inverter)

        self.canvas.tag_bind(self.tag + "activate_together", "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.tag + "activate_together", "<Leave>", self.on_leave)

    def on_enter(self, event):
        active_outline_width = self.canvas.itemcget("scale_on_zoom_2_5", "activewidth")
        self.canvas.itemconfigure(self.perimeter, outline='orange', width=active_outline_width)
        self.canvas.itemconfigure(self.output_connection['OUT_0'].output_inverter, outline='orange', width=active_outline_width)

    def on_leave(self, event):
        outline_width = self.canvas.itemcget("scale_on_zoom_2_5", "width")
        self.canvas.itemconfigure(self.perimeter, outline='blue', width=outline_width)
        self.canvas.itemconfigure(self.output_connection['OUT_0'].output_inverter, outline='blue', width=outline_width)

    def update_state(self):
        self.output_connection['OUT_0'].state = not self.input_connection['IN_0'].state


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
        self.canvas.addtag_withtag(self.tag + "dragable", self.perimeter)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # An AND gate has two input connections and one output connection
        self.input_connection['IN_0'] = InputConnection(self, 'Input 0')
        self.input_connection['IN_1'] = InputConnection(self, 'Input 1')
        self.output_connection['OUT_0'] = OutputConnection(self, (x + 60, y + 30), 'Output')

        # Ensure initial value of output is correct
        self.update_state()

    def update_state(self):
        self.output_connection['OUT_0'].state = self.input_connection['IN_0'].state and self.input_connection['IN_1'].state


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
        self.canvas.addtag_withtag(self.tag + "dragable", self.perimeter)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # An OR gate has two input connections and one output connection
        self.input_connection['IN_0'] = InputConnection(self, 'Input 0')
        self.input_connection['IN_1'] = InputConnection(self, 'Input 1')
        self.output_connection['OUT_0'] = OutputConnection(self, (x + 65, y + 30), 'Output')

        # Ensure initial value of output is correct
        self.update_state()

    def update_state(self):
        self.output_connection['OUT_0'].state = self.input_connection['IN_0'].state or self.input_connection['IN_1'].state


class XOrGate(Gate):
    """The XOR Gate draws itself on a canvas"""

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
        self.canvas.addtag_withtag(self.tag + "dragable", self.perimeter)


        points = []
        points.extend((x - 8, y))  # first point in polygon

        for angle in range(-90, 90):
            arc_x = (math.cos(math.radians(angle)) * 8) + (x - 8)
            arc_y = (math.sin(math.radians(angle)) * 30) + (y + 30)
            points.extend((arc_x, arc_y))

        for angle in range(90, 270):
            arc_x = (math.cos(math.radians(angle)) * -8) + (x - 8)
            arc_y = (math.sin(math.radians(angle)) * 30) + (y + 30)
            points.extend((arc_x, arc_y))

        self.polyarc = canvas.create_polygon(points, outline='blue', activeoutline='orange',
                                               fill='', width=2, activewidth=5, tags=name_tag)

        self.canvas.addtag_withtag("scale_on_zoom_2_5", self.polyarc)
        self.canvas.addtag_withtag(self.tag + "dragable", self.polyarc)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # An XOR gate has two input connections and one output connection
        self.input_connection['IN_0'] = InputConnection(self, 'Input 0')
        self.input_connection['IN_1'] = InputConnection(self, 'Input 1')
        self.output_connection['OUT_0'] = OutputConnection(self, (x + 65, y + 30), 'Output')

        # Ensure initial value of output is correct
        self.update_state()

        # Tag the specific canvas items we want to activate (highlight) together
        self.canvas.addtag_withtag(self.tag + "activate_together", self.perimeter)
        self.canvas.addtag_withtag(self.tag + "activate_together", self.polyarc)

        self.canvas.tag_bind(self.tag + "activate_together", "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.tag + "activate_together", "<Leave>", self.on_leave)

    '''
    Because we have a canvas object composed of multiple items, we can no longer depend on
    the default enter/activate leave/deactive of the item, as it would only "light up" part
    of the object.  I couldn't find any way to forcibly "activate" another item to cause its
    activewidth and activeoutline parameters to "go active" artificially, so came up with
    the following on_enter and on_leave event handlers to do the work manually.

    We first (on_enter) sample an item tagged with "scale_on_zoom_2_5" and then set that new
    width on the items of the gate object, along with the desired active color.  This happens
    if we enter either item composing the compound object.

    When the pointer exits the item (on_leave) we reset the width and color back.

    The only problem with this method currently is that while zooming, if the pointer is within
    one of the items, the width and activewidth change, but these callbacks are not triggered
    since the pointer never leaves the item.  This leaves one of the items displaying a slightly
    different width.  It's a minor visual annoyance, that I'm not going to care about for now.
    '''

    def on_enter(self, event):
        self.canvas.tag_raise(self.perimeter)
        active_outline_width = self.canvas.itemcget("scale_on_zoom_2_5", "activewidth")
        self.canvas.itemconfigure(self.polyarc, outline='orange', width=active_outline_width)
        self.canvas.itemconfigure(self.perimeter, outline='orange', width=active_outline_width)
        self.canvas.update_idletasks()

    def on_leave(self, event):
        outline_width = self.canvas.itemcget("scale_on_zoom_2_5", "width")
        self.canvas.itemconfigure(self.polyarc, outline='blue', width=outline_width)
        self.canvas.itemconfigure(self.perimeter, outline='blue', width=outline_width)

    def update_state(self):
        # Python does not implement a logical XOR operator, but because we are storing
        # state using the Boolean type, we can use the Bitwise XOR operator here
        self.output_connection['OUT_0'].state = self.input_connection['IN_0'].state ^ self.input_connection['IN_1'].state



