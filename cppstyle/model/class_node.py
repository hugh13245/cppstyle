from .node import Node


class Class(Node):
    def __init__(self, file, position, access, name, children):
        super(Class, self).__init__(file, position, access, children)
        self.name = name