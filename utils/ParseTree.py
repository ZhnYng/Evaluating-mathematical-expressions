from ADT import Stack, BinaryTree, Hashtable
import re

class ParseTree:
    def __init__(self):
        self.statements = Hashtable() # Stores statements and their expression trees
        self.active_evaluations = set()

    def buildParseTree(self, exp):
        tokens = re.findall(r'[\d.]+|\w+|[^\s\w]', exp)
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        currentTree = tree
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t.isnumeric():
                currentTree.setKey(int(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If token is a letter, set key of the current node
            # to that letter and return to parent
            elif t.isalpha():
                currentTree.setKey(t)
                parent = stack.pop()
                currentTree = parent

            # RULE 5: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self, var, tree:BinaryTree):
        if var in self.active_evaluations:
            raise ValueError(f"Circular dependency detected for variable: {var}")
        
        self.active_evaluations.add(var)
        result = self.evaluate_expression(tree)
        if result == 'None':
            self.active_evaluations.clear()
        else:
            self.active_evaluations.remove(var)    
        return result
        
    def evaluate_expression(self, tree:BinaryTree):
        if tree:
            if tree.getLeftTree() and tree.getRightTree():
                op = tree.getKey()
                left = self.evaluate_expression(tree.getLeftTree())
                right = self.evaluate_expression(tree.getRightTree())
                if left == 'None' or right == 'None': return 'None'
                elif op == '+': return left + right
                elif op == '-': return left - right
                elif op == '*': return left * right
                elif op == '/': return left / right
            else:
                # Handle statements and numbers
                key = tree.getKey()
                if isinstance(key, int):
                    return key
                elif key in self.statements:
                    return self.evaluate(key, self.statements[key])
                else:
                    return 'None'

    def add_statement(self, var, exp):
        tree = self.buildParseTree(exp)
        self.statements[var] = tree