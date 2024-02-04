import matplotlib.pyplot as plt
import networkx as nx
from AbstractClasses import Tree

class PrintableTree(Tree):
    def __init__(self, key, digraph):
        super().__init__(key)
        self.pos = None  # Graphical attributes
        self.G = digraph

    def get_depth(self):
        def depth(node):
            if not node.children:
                return 1
            return 1 + max(depth(child) for child in node.children)
        return depth(self)

    def build_graph(self, pos={}, x=0, y=0, layer=1, width=1.5):
        # Adjusted the default width to a smaller value
        total_depth = self.get_depth()
        layer_height = -1.5  # Adjust vertical spacing to grow downwards, potentially smaller than before

        if layer == 1:
            # Adjust initial width based on depth to prevent overlap, may need to be fine-tuned
            width = max(2 ** (total_depth - 1), 1.5)

        pos[self.key] = (x, y)
        self.G.add_node(self.key)
        
        if self.children:
            num_children = len(self.children)
            spacing = width / max(num_children, 1)
            new_x = x - width / 2 + spacing / 2
            for child in self.children:
                self.G.add_edge(self.key, child.key)
                child.build_graph(pos, new_x, y + layer_height, layer + 1, spacing)  # Adjust y to grow downwards
                new_x += spacing

        self.pos = pos

    def display_graph(self):
        plt.figure(figsize=(8, 6))  # Adjusted to a smaller figure size
        self.build_graph()
        nx.draw(self.G, self.pos, with_labels=True, arrows=False, node_size=500, node_color='lightblue', font_size=10, edge_color='gray')
        plt.axis('equal')  # Ensure the scaling is equal to make the tree more symmetric
        plt.show()