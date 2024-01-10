from ADT import Stack, BinaryTree, Hashtable

class ParseTree:
    def __init__(self):
        self.statements = Hashtable()
        # self.statements = {}  # Stores statements and their expression trees

    def buildParseTree(self, exp):
        tokens = [token for token in exp]
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
            elif t not in ['(', '+', '-', '*', '/', ')'] and t.isnumeric():
                currentTree.setKey(int(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If token is a letter, set key of the current node
            # to that letter and return to parent
            elif t not in ['(', '+', '-', '*', '/', ')'] and t.isalpha():
                currentTree.setKey(t)
                parent = stack.pop()
                currentTree = parent

            # RULE 5: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self, tree):
        if tree:
            if tree.getLeftTree() and tree.getRightTree():
                op = tree.getKey()
                left = self.evaluate(tree.getLeftTree())
                right = self.evaluate(tree.getRightTree())
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
                elif key in self.statements: # Error in hashing here
                    return self.evaluate(self.statements[key])
                else:
                    return 'None'

    def add_statement(self, var, exp):
        # Check for circular dependency
        for char in exp:
            if char.isalpha() and char in self.statements:
                raise ValueError(f"Circular dependency detected for variable {var}. Variable {char} is dependent on variable {var}")

        if var in exp or var in self.statements:
            raise ValueError("Circular dependency detected for variable " + var)
        
        tree = self.buildParseTree(exp)
        self.statements[var] = tree

# Usage
# pt = ParseTree()
# pt.addVariable("b", "(1+5)")
# pt.addVariable("a", "(1+b)")

# result_a = pt.evaluate(pt.statements["a"])
# print("Value of a:", result_a)