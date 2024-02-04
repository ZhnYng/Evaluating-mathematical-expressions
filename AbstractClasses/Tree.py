class Tree:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_child(self, child):
        self.children.append(child)