from ADT import Stack, BinaryTree, Hashtable
import re

class ParseTree:
    """
    A class for constructing and evaluating expression parse trees.

    The ParseTree class supports building a binary tree from a mathematical expression,
    evaluating that expression, and handling variable assignments and references within expressions.
    It uses a hashtable for memoization to optimize repeated evaluations and to handle circular dependencies.

    Attributes:
        statements (Hashtable): Stores variable assignments and their corresponding expression trees.
        memoization_cache (Hashtable): Cache used to store previously computed results for optimization.
        active_evaluations (set): Tracks variables currently being evaluated to detect circular dependencies.
    """

    def __init__(self):
        """Initialize the ParseTree with empty statements and memoization cache."""
        self.statements = Hashtable()  # Stores statements and their expression trees
        self.memoization_cache = Hashtable()  # Cache for memoization
        self.active_evaluations = set()

    def buildParseTree(self, exp_tokens):
        """
        Constructs a parse tree for the given expression tokens.

        This method constructs a binary tree based on the tokens of a mathematical expression. It follows
        specific rules to place tokens in the tree, handling operators, numbers, variables, and parentheses.

        Parameters:
            exp_tokens (list of str): Tokens of the mathematical expression to be parsed.

        Returns:
            BinaryTree: The root node of the constructed parse tree.

        Raises:
            ValueError: If an unexpected token is encountered.
        """
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        currentTree = tree
            
        for t in exp_tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
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

            # RULE 5: If token is a float, set key of the current node
            # to that float and return to parent
            elif t.replace(".", "").isnumeric():
                currentTree.setKey(float(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 6: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self, var, tree: BinaryTree):
        """
        Evaluates the expression represented by the parse tree for a given variable.

        This method computes the value of the expression tree, handling variables,
        operators, and function calls. It checks for circular dependencies and uses memoization
        for optimization.

        Parameters:
            var (str): The variable name associated with the expression being evaluated.
            tree (BinaryTree): The root of the expression parse tree.

        Returns:
            float or int: The evaluated result of the expression.

        Raises:
            ValueError: If a circular dependency is detected.
        """
        if var in self.active_evaluations:
            self.active_evaluations.clear()
            raise ValueError(f"Circular dependency detected for variable: {var}")
        
        # Check cache first before evaluating
        if var in self.memoization_cache:
            return self.memoization_cache[var]
        
        self.active_evaluations.add(var)
        result = self.evaluate_expression(tree)

        if isinstance(result, float):
            result = round(result, 4)  # Round off floating-point calculations
        
        # Clear active evaluations appropriately
        if result == 'None':
            self.active_evaluations.clear()
        else:
            self.active_evaluations.remove(var)
            self.memoization_cache[var] = result  # Cache the result
        
        return result
        
    def evaluate_expression(self, tree:BinaryTree):
        """
        Recursively evaluates the given expression tree.

        This method traverses the tree, evaluating the expression based on the operators and operands
        defined in the tree nodes. It handles arithmetic operations and variable references.

        Parameters:
            tree (BinaryTree): The root of the expression tree to evaluate.

        Returns:
            float or int or 'None': The result of the expression evaluation, or 'None' if a variable is undefined.

        Raises:
            ZeroDivisionError: If the expression includes division by zero.
        """
        if tree:
            if tree.getLeftTree() and tree.getRightTree():
                op = tree.getKey()
                left = self.evaluate_expression(tree.getLeftTree())
                right = self.evaluate_expression(tree.getRightTree())
                if left == 'None' or right == 'None': return 'None'
                elif op == '+': return left + right
                elif op == '-': return left - right
                elif op == '*': return left * right
                elif op == '/': 
                    if right == 0:
                        raise ZeroDivisionError('You have provided an expression with a divisor of 0')
                    return left / right
                elif op == '**': return left ** right
            else:
                # Handle statements and numbers
                key = tree.getKey()
                if key == '?': raise RuntimeError('Error evaluating expression due to missing operand or operand.') # '?' is the default key value for initiating a tree
                
                if isinstance(key, int) or isinstance(key, float):
                    return key
                elif key in self.statements:
                    return self.evaluate(key, self.statements[key])
                else:
                    return 'None'

    def add_statement(self, var, exp_tokens):
        """
        Adds a new variable assignment statement to the parse tree.

        This method constructs a parse tree for the given expression tokens and associates it
        with a variable name. It checks for circular dependencies before adding the statement.

        Parameters:
            var (str): The variable name for the assignment.
            exp_tokens (list of str): Tokens of the mathematical expression to be assigned to the variable.

        Raises:
            ValueError: If a circular dependency is detected.
        """
        tree = self.buildParseTree(exp_tokens)
        if var in self.memoization_cache:
            del self.memoization_cache[var] # Delete cache as expression has changed
        self.statements[var] = tree
        
        try:
            self.evaluate(var, tree) # Evaluate to test for circular dependency
        except ValueError:
            del self.statements[var]
            raise ValueError(f"Circular dependency detected for variable: {var}")