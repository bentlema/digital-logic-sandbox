

class Wire:

    def __init__(self, canvas, name_tag):
        """ pass in the canvas object id so we know where to draw our wire"""

        # Remember the canvas that I'm drawn on
        self.canvas = canvas

        # my primary name tag
        self.tag = name_tag

        # points to draw the line, and the line itself
        self.starting_point = (0, 0)
        self.ending_point = (0, 0)
        self.line_item = None

        self.midpoint1 = (0, 0)
        self.midpoint2 = (0, 0)

        # Dictionaries to keep track of inputs and outputs
        self.input_connection = {}
        self.output_connection = {}

        # These will point to the input and output connections once connected a Gate
        self.input_connection['IN_0'] = None
        self.output_connection['OUT_0'] = None

    def update_state(self):
        self.output_connection['OUT_0'].state = self.input_connection['IN_0'].state

    def connect(self, input, output):
        # input  - gate or circuit component input
        # output - gate or circuit component output
        #
        # We are connecting the output of one gate to the input of another gate
        # We must pass in the outputConnection object and the inputConnection object
        self.input_connection['IN_0'] = input     # the upstream circuit component output
        self.output_connection['OUT_0'] = output  # the downstream circuit component input
        self.input_connection['IN_0'].parent.register_connection(self)
        self.output_connection['OUT_0'].parent.register_connection(self)
        self.draw()

    def draw(self):

        if self.line_item is not None:
            self.canvas.delete(self.line_item)

        if (self.input_connection['IN_0'] is not None) and (self.output_connection['OUT_0'] is not None):
            current_width = float(self.canvas.itemcget("scale_on_zoom_2_2", "width"))

            # Calculate the center of the circle point
            starting_point_x = (self.input_connection['IN_0'].get_location()[0] + self.input_connection['IN_0'].get_location()[2]) // 2
            starting_point_y = (self.input_connection['IN_0'].get_location()[1] + self.input_connection['IN_0'].get_location()[3]) // 2

            # We introduce a couple mid-points and the smooth=True option to give us a nice curved line
            # We use a base x-shift of 20, but then scale that based on the current_width so that it works when zooming
            midpoint1_x = starting_point_x + int(current_width * 20)
            midpoint1_y = starting_point_y

            # Calculate the center of the circle point
            ending_point_x = (self.output_connection['OUT_0'].get_location()[0] + self.output_connection['OUT_0'].get_location()[2]) // 2
            ending_point_y = (self.output_connection['OUT_0'].get_location()[1] + self.output_connection['OUT_0'].get_location()[3]) // 2

            # We introduce a couple mid-points and the smooth=True option to give us a nice curved line
            # We use a base x-shift of -20, but then scale that based on the current_width so that it works when zooming
            midpoint2_x = ending_point_x - int(current_width * 20)
            midpoint2_y = ending_point_y

            # These are the 4 points we will use to draw our line
            self.starting_point = (starting_point_x, starting_point_y)
            self.midpoint1 = (midpoint1_x, midpoint1_y)
            self.midpoint2 = (midpoint2_x, midpoint2_y)
            self.ending_point = (ending_point_x, ending_point_y)

            #current_width = self.canvas.itemcget("scale_on_zoom_2_2", "width")
            self.line_item = self.canvas.create_line(self.starting_point, self.midpoint1, self.midpoint2, self.ending_point, width=current_width, fill='blue', capstyle="round", smooth=True)
            self.canvas.addtag_withtag("scale_on_zoom_2_2", self.line_item)


