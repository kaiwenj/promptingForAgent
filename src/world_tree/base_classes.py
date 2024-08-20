from anytree import NodeMixin

class Location(NodeMixin):
    def __init__(self, name, parent=None):
        self.name = name
        self.type = "location"
        self.contents = []
        self.actors = []
        self.parent = parent

    def add_content(self, content):
        self.contents.append(content)
        content.parent = self

class Object(NodeMixin):
    def __init__(self, name, status="None", parent=None):
        self.name = name
        self.type = "object"
        self.status = status
        self.contents = []
        self.parent = parent

    def add_content(self, content):
        self.contents.append(content)
        content.parent = self
