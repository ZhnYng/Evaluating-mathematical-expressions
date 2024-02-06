# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# A class for constructing and evaluating expression parse trees.
# The ParseTree class supports building a binary tree from a mathematical expression,
# evaluating that expression, and handling variable assignments and references within expressions.
# It uses a hashtable to optimize repeated evaluations and to handle circular dependencies.
# Attributes:
#     statements (Hashtable): Stores variable assignments and their corresponding expression trees.
#     active_evaluations (set): Tracks variables currently being evaluated to detect circular dependencies.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : ParseTree.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
from ADT import Stack, BinaryTree, Hashtable

class ParseTree:
    """
    A class for constructing and evaluating expression parse trees.

    The ParseTree class supports building a binary tree from a mathematical expression,
    evaluating that expression, and handling variable assignments and references within expressions.
    It uses a hashtable to optimize repeated evaluations and to handle circular dependencies.

    Attributes:
        statements (Hashtable): Stores variable assignments and their corresponding expression trees.
        active_evaluations (set): Tracks variables currently being evaluated to detect circular dependencies.
    """

    def __init__(self):
        """Initialize the ParseTree with empty statements."""
        self.__statements = Hashtable()  # Stores statements and their expression trees
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

    def build_parse_tree(self, exp_tokens):
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
        current_tree = tree
            
        for t in exp_tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == '(':
                current_tree.insert_left('?')
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()

            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
                current_tree.set_key(t)
                current_tree.insert_right('?')
                stack.push(current_tree)
                current_tree = current_tree.get_right_tree()

            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t.isnumeric():
                current_tree.set_key(int(t))
                parent = stack.pop()
                current_tree = parent

            # RULE 4: If token is a letter, set key of the current node
            # to that letter and return to parent
            elif t.isalpha():
                current_tree.set_key(t)
                parent = stack.pop()
                current_tree = parent

            # RULE 5: If token is a float, set key of the current node
            # to that float and return to parent
            elif t.replace(".", "").isnumeric():
                current_tree.set_key(float(t))
                parent = stack.pop()
                current_tree = parent

            # RULE 6: If token is ')' go to parent of current node
            elif t == ')':
                current_tree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self, var, tree: BinaryTree):
        """
        Evaluates the expression represented by the parse tree for a given variable.

        This method computes the value of the expression tree, handling variables,
        operators, and function calls. It checks for circular dependencies.

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
        
        # Add variable to active evaluations to track circular dependencies
        self.__active_evaluations.add(var)
        
        # Evaluate the expression tree
        result = self.__evaluate_expression(tree)

        # Round off floating-point calculations
        if isinstance(result, float):
            result = round(result, 2)
        
        # Clear active evaluations if the result is 'None', otherwise remove variable from active evaluations
        if result == 'None':
            self.__active_evaluations.clear()
        else:
            self.__active_evaluations.remove(var)  # Remove variable from active evaluations
        return result
        
    def __evaluate_expression(self, tree: BinaryTree):
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
            if tree.get_left_tree() and tree.get_right_tree():
                op = tree.get_key()  # Get the operator
                left = self.__evaluate_expression(tree.get_left_tree())  # Evaluate left subtree
                right = self.__evaluate_expression(tree.get_right_tree())  # Evaluate right subtree
                
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
        tree = self.build_parse_tree(exp_tokens)
        
        # Associate the parse tree with the variable
        self.__statements[var] = tree
        
        # Check for circular dependencies
        try:
            self.evaluate(var, tree)
        except ValueError:
            # Roll back the addition if a circular dependency is detected
            del self.__statements[var]
            raise ValueError(f"Circular dependency detected for variable: {var}")