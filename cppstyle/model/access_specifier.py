from .node import Node


class AccessSpecifier(Node):
    def __init__(self, file, position, access, children):
        super(AccessSpecifier, self).__init__(file, position, access, children)
