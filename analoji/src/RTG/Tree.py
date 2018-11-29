class Tree():
    ''' Tree class to help generalize decomposing terms in analogies '''

    def __init__(self, name, value, children = []):
        ''' constructor for tree '''
        self.name = name
        self.data = value
        self.children = children
        self.child_count = self.set_child_count(self.children)

    def __repr__(self):
        ''' string representation of tree '''
        return "Tree object for {}".format(self.name)

    def set_name(self, payload):
        ''' sets name attribute to payload parameter '''
        self.name = payload

    def set_data(self, payload):
        ''' sets data attribute to payload parameter '''
        self.data = payload

    def set_children(self, payload):
        ''' sets children attribute to payload parameter '''
        self.children = payload

    def set_child_count(self, payload):
        ''' sets children_count attribute to payload parameter '''
        self.child_count = payload

    def get_name(self):
        ''' gets name attribute '''
        return self.name

    def get_data(self):
        ''' gets data attribute '''
        return self.data

    def get_children(self):
        ''' gets children attribute '''
        return self.children

    def get_child_count(self):
        ''' gets children_count attribute '''
        return self.child_count