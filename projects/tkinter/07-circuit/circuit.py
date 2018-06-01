
""" A Circuit object knows about, or 'contains', all of the individual circuit component objects.
    We need to keep in mind that this object will eventually be used as a way to create a
    black-box / integrated circuit, where we can have individual instances of a circuit.  For
    example, we can implement an adder, and then create an adder IC, and then instantiate
    multiple adder ICs within another circuit.  This is how we can build up more complex circuits.

    So when we create a circuit component (such as a gate), we need to tell it what circuit it
    is a part of.  This will need to be a new parameter passed upon component create.  Or should
    we call methods on a circuit to create the sub-components? That would seem like the more
    object-oriented way to do it, as the circuit 'contains' the gates and wires. """



class Circuit:

    def __init__(self, canvas):
        """ We need a data structure to keep track of the objects in our circuit
            specifically so that we can refresh (re-draw) the entire canvas with
            all of its objects.  This is being driven by the 'select multiple objects'
            feature, as we currently have no way to reference gates when we select
            multiple gates and drag one of them, there is no way to reference and
            update the wires attach to the gate objects being dragged indirectly. """

        # Remember the canvas that I'm drawn on
        self.canvas = canvas

        # Should this be an array or a dictionary?
        self.circuit_components = {}

        # Our Circuit should have a name
        self.name = ""


    def set_name(self, name):
        self.name = name
        print("Setting Circuit Name to: {}".format(name))

    def register_circuit_component(self, component, name):
        print("Registering component {} with name_tag {}".format(component, name))
        self.circuit_components[name] = component

    def update_connections(self):
        for cc in self.circuit_components:
            #print("update_connections() - Circuit Component: {} = {}".format(cc, self.circuit_components[cc]))
            self.circuit_components[cc].update_connections()

    def draw_all(self):
        # For each circuit component, loop through, and call it's draw method.
        # As gates do not currently have a draw() method, we need to implement that
        # except, we dont have a draw method yet--we are relying on canvas methods
        # to manipulate items
        pass

