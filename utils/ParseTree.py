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
        self.__statements = Hashtable()  # Stores statements and their expression trees
        self.__memoization_cache = Hashtable()  # Cache for memoization
        self.__active_evaluations = set() # Storage for catching circular dependencies

    def get_statements(self):
        """
        Retrieves the statements stored in the ParseTree.

        Returns:
            Hashtable: A hashtable containing the statements and their associated expression trees.
        """
        return self.__statements
    
    def set_statements(self, statements):
        """
        Sets the statements of the ParseTree.

        Parameters:
            statements (Hashtable): A hashtable containing the statements and their associated expression trees.
        """
        self.__statements = statements
    
    def get_memoization_cache(self):
        """
        Retrieves the memoization cache stored in the ParseTree.

        Returns:
            Hashtable: A hashtable containing the memoization cache.
        """
        return self.__memoization_cache
    
    def set_memoization_cache(self, memoization_cache):
        """
        Sets the memoization cache of the ParseTree.

        Parameters:
            memoization_cache (Hashtable): A hashtable containing the memoization cache.
        """
        self.__memoization_cache = memoization_cache
    
    def get_active_evaluations(self):
        """
        Retrieves the set of active evaluations stored in the ParseTree.

        Returns:
            set: A set containing the active evaluations.
        """
        return self.__active_evaluations
    
    def set_active_evaluations(self, active_evaluations):
        """
        Sets the set of active evaluations of the ParseTree.

        Parameters:
            active_evaluations (set): A set containing the active evaluations.
        """
        self.__active_evaluations = active_evaluations

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
                currentTree.set_key(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t.isnumeric():
                currentTree.set_key(int(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If token is a letter, set key of the current node
            # to that letter and return to parent
            elif t.isalpha():
                currentTree.set_key(t)
                parent = stack.pop()
                currentTree = parent

            # RULE 5: If token is a float, set key of the current node
            # to that float and return to parent
            elif t.replace(".", "").isnumeric():
                currentTree.set_key(float(t))
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
        # Check for circular dependency
        if var in self.__active_evaluations:
            self.__active_evaluations.clear()  # Clear active evaluations to avoid infinite recursion
            raise ValueError(f"Circular dependency detected for variable: {var}")
        
        # Check cache first before evaluating
        if var in self.__memoization_cache:
            return self.__memoization_cache[var]
        
        # Add variable to active evaluations to track circular dependencies
        self.__active_evaluations.add(var)
        
        # Evaluate the expression tree
        result = self.evaluate_expression(tree)

        # Round off floating-point calculations
        if isinstance(result, float):
            result = round(result, 4)
        
        # Clear active evaluations if the result is 'None', otherwise remove variable from active evaluations
        if result == 'None':
            self.__active_evaluations.clear()
        else:
            self.__active_evaluations.remove(var)  # Remove variable from active evaluations
            self.__memoization_cache[var] = result  # Cache the result
        
        return result
        
    def evaluate_expression(self, tree: BinaryTree):
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
        # Check if the tree is not empty
        if tree:
            # Check if both left and right subtrees exist
            if tree.getLeftTree() and tree.getRightTree():
                op = tree.get_key()  # Get the operator
                left = self.evaluate_expression(tree.getLeftTree())  # Evaluate left subtree
                right = self.evaluate_expression(tree.getRightTree())  # Evaluate right subtree
                
                # Return 'None' if either operand is 'None'
                if left == 'None' or right == 'None':
                    return 'None'
                # Evaluate the expression based on the operator
                elif op == '+': return left + right
                elif op == '-': return left - right
                elif op == '*': return left * right
                elif op == '/':
                    # Check for division by zero
                    if right == 0:
                        raise ZeroDivisionError('Division by zero error')
                    return left / right
                elif op == '**': return left ** right
            else:
                # Handle leaf nodes (operands or variables)
                key = tree.get_key()
                # Return error if the default key is encountered
                if key == '?':
                    raise RuntimeError('Error evaluating expression due to missing operand or operator.')
                # Return the operand if it's a number
                if isinstance(key, int) or isinstance(key, float):
                    return key
                # Evaluate variable reference
                elif key in self.__statements:
                    return self.evaluate(key, self.__statements[key])
                # Return 'None' for undefined variables
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
        # Build the parse tree from the expression tokens
        tree = self.buildParseTree(exp_tokens)
        
        # Remove cached result if the expression has changed
        if var in self.__memoization_cache:
            del self.__memoization_cache[var]
        
        # Associate the parse tree with the variable
        self.__statements[var] = tree
        
        # Check for circular dependencies
        try:
            self.evaluate(var, tree)
        except ValueError:
            # Roll back the addition if a circular dependency is detected
            del self.__statements[var]
            raise ValueError(f"Circular dependency detected for variable: {var}")
        
    def full_tree(self, var):
        """
        Parses and connects the entire tree, including resolving variable dependencies.

        This method constructs a comprehensive parse tree that includes all dependencies
        by connecting parse trees of variables referenced within expressions.

        Parameters:
            var (str): The root variable name from which to begin parsing and connecting the tree.

        Returns:
            BinaryTree: The root node of the fully connected parse tree, including all dependencies.

        Raises:
            ValueError: If a variable is undefined or a circular dependency is detected.
        """
        # Function to recursively connect the trees
        def connect_trees(tree:BinaryTree):
            if tree:
                key = tree.get_key()
                if isinstance(key, str):
                    if key in self.__statements:
                        # Replace the current tree node with the tree from statements
                        # if the key is a variable name, effectively connecting trees
                        connected_tree = self.__statements[key]
                        tree.set_key(f"{tree.get_key()} ({connected_tree.get_key()})")
                        tree.insertLeft(connect_trees(connected_tree.getLeftTree()).get_key())
                        tree.insertRight(connect_trees(connected_tree.getRightTree()).get_key())
                    else:
                        # If the node is not a variable, recursively check its subtrees
                        connect_trees(tree.getLeftTree())
                        connect_trees(tree.getRightTree())
            return tree

        # Connect the trees starting from the root variable's tree
        connected_tree_root = connect_trees(self.__statements[var].copy())
        return connected_tree_root