from anytree import NodeMixin

class Location(NodeMixin):
    def __init__(self, name, parent=None):
        self.name = name
        self.type = "location"
        self.parent = parent

class Object(NodeMixin):
    def __init__(self, name, status="None", parent=None):
        self.name = name
        self.type = "object"
        self.status = status
        self.parent = parent