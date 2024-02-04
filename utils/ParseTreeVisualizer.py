import networkx as nx
from ADT import PrintableTree, BinaryTree

class ParseTreeVisualizer:
    def __init__(self, binary_tree):
        self.binary_tree = binary_tree
        self.visual_tree = None
        self.G = nx.DiGraph()

    def convert_to_visual_tree(self, node:BinaryTree, digraph):
        if node is None:
            return None
        visual_node = PrintableTree(node.get_key(), digraph)
        if node.getLeftTree():
            visual_node.add_child(self.convert_to_visual_tree(node.getLeftTree(), digraph))
        if node.getRightTree():
            visual_node.add_child(self.convert_to_visual_tree(node.getRightTree(), digraph))
        return visual_node

    def display(self):
        self.visual_tree = self.convert_to_visual_tree(self.binary_tree, self.G)
        if self.visual_tree:
            self.visual_tree.display_graph()
        else:
            print("Statement does not exist.")