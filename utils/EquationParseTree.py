# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Class representing a set of options for manipulating assignment statements and equations.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : EquationParseTree.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
from ADT import Stack, BinaryTree, Hashtable
from utils import ParseTree

class EquationParseTree(ParseTree):
    """
    A class for constructing and evaluating equation parse trees. E.g. (x+2)=(y+3)

    The EquationParseTree class supports building a binary tree from a mathematical equation,
    evaluating that expression, and handling variable assignments and references within expressions.
    It uses a hashtable for memoization to optimize repeated evaluations and to handle 
    circular dependencies inherited from ParseTree.

    Attributes:
        equations (Hashtable): Stores variable assignments and their corresponding expression trees.
        memoization_cache (Hashtable): Cache used to store previously computed results for optimization.
        active_evaluations (set): Tracks variables currently being evaluated to detect circular dependencies.
    """

    def __init__(self):
        super().__init__()
        self.__equations = Hashtable()
        self.__memoization_cache = Hashtable()
        self.__active_evaluations = set()
        self.__supported_operators = ['+', '-', '*', '/']

    # Getter method for __equations
    def get_equations(self):
        return self.__equations

    # Setter method for __equations
    def set_equations(self, equations):
        self.__equations = equations

    # Getter method for __memoization_cache
    def get_memoization_cache(self):
        return self.__memoization_cache

    # Setter method for __memoization_cache
    def set_memoization_cache(self, memoization_cache):
        self.__memoization_cache = memoization_cache

    # Getter method for __active_evaluations
    def get_active_evaluations(self):
        return self.__active_evaluations

    # Setter method for __active_evaluations
    def set_active_evaluations(self, active_evaluations):
        self.__active_evaluations = active_evaluations

    def build_parse_tree(self, eqn_tokens):
        """
        Constructs a Equation parse tree for the given expression tokens.
        An equation parse tree is a tree representation of a DoubleStatement e.g. (x+2)=(y+3)

        This method constructs a binary tree based on the tokens of a mathematical expression. It follows
        specific rules to place tokens in the tree, handling operators, numbers, variables, and parentheses.

        Parameters:
            eqn_tokens (list of str): Tokens of the mathematical statement to be parsed.

        Returns:
            BinaryTree: The root node of the constructed parse tree.

        Raises:
            ValueError: If an unexpected token is encountered.
        """
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        current_tree = tree
            
        for index, t in enumerate(eqn_tokens):
            # RULE 1: If token is '(' and the previous token is '='
            # insert a node to the left and descend into that node
            if t == '(' and eqn_tokens[index-1] == '=':
                current_tree.insert_left('?')
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()

            # RULE 2: If token is '(' add a new node as left child
            # and descend into that node
            elif t == '(':
                current_tree.insert_left('?')
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()
                current_tree.insert_left('?')
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()

            # RULE 3: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
                current_tree.set_key(t)
                current_tree.insert_right('?')
                stack.push(current_tree)
                current_tree = current_tree.get_right_tree()

            # RULE 4: If token is number, set key of the current node
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

            # RULE 7: If token is '=', set key to '=', insert a node on the right
            # and descend into that node
            elif t == '=':
                current_tree.set_key(t)
                current_tree.insert_right('?')
                stack.push(current_tree)
                current_tree = current_tree.get_right_tree()
            else:
                raise ValueError
        return tree
    
    def evaluate_equation(self, tree: BinaryTree, past_statements):
        """
        Evaluates the expression represented by the parse tree for a given variable.

        This method computes the value of the expression tree, handling variables,
        operators, and function calls. It checks for circular dependencies and uses memoization
        for optimization. The main difference between this and the ParseTree evaluate function
        is the ability to check the equality of two expressions, where '=' is treated as an operator.

        Parameters:
            tree (BinaryTree): The root of the expression parse tree.
            past_statements (dict): Dictionary containing variable assignments and their evaluated values from ParseTree.

        Returns:
            float or int: The evaluated result of the expression.

        Raises:
            ValueError: If a circular dependency is detected.
        """
        
        # Evaluate the expression tree
        result = self.__evaluate_equation(tree, past_statements)

        # Round off floating-point calculations
        if isinstance(result, float):
            result = round(result, 2)

        return result
        
    def __evaluate_equation(self, tree: BinaryTree, past_statements):
        """
        Recursively evaluates the given equation tree.

        This method traverses the tree, evaluating the equation based on the operators and operands
        defined in the tree nodes. It handles arithmetic operations and variable references.
        The '=' is an operator here, which evaluates the equality of the two expressions in the equation.

        Parameters:
            tree (BinaryTree): The root of the expression tree to evaluate.
            past_statements (dict): Dictionary containing variable assignments and their evaluated values.

        Returns:
            bool or None: True if the equation is equal, False if not equal, or None if a variable is undefined.

        Raises:
            ZeroDivisionError: If the expression includes division by zero.
            RuntimeError: If the expression tree encounters a missing operand or operator.
        """
        # Check if the tree is not empty
        if tree:
            # Check if both left and right subtrees exist
            if tree.get_left_tree() and tree.get_right_tree():
                op = tree.get_key()  # Get the operator
                left = self.__evaluate_equation(tree.get_left_tree(), past_statements)  # Evaluate left subtree
                right = self.__evaluate_equation(tree.get_right_tree(), past_statements)  # Evaluate right subtree
                
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
                elif op == '=': return left == right  # Evaluate equality of two expressions
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
                elif key in past_statements:
                    # Try to evaluate variables from ParseTree class
                    # evaluate and statements inherited from ParseTree
                    return self.evaluate(key, past_statements[key])
                # Return 'None' for undefined variables
                else:
                    return 'None'

    def add_statement(self, eqn_tokens):
        """
        Adds a new variable assignment statement to the parse tree.

        This method constructs a parse tree for the given expression tokens and associates it
        with a variable name. It checks for circular dependencies before adding the statement.

        Parameters:
            var (str): The variable name for the assignment.
            eqn_tokens (list of str): Tokens of the mathematical expression to be assigned to the variable.

        Returns:
            str: The unique identifier of the equation.

        Raises:
            None (No circular dependency possible)
        """
        # Give the equation a unique id
        id = f"Equation {len(self.__equations)+1}"
        # Build the parse tree from the expression tokens
        tree = self.build_parse_tree(eqn_tokens)
        
        # Remove cached result if the expression has changed
        if id in self.__memoization_cache:
            del self.__memoization_cache[id]
        
        # Associate the parse tree with the variable
        self.__equations[id] = tree
        return id
        
    def rearrange_tree(self, target_variable, equation_tree:BinaryTree):
        """
        Rearranges an equation to make a specified variable the subject.

        Parameters:
            target_variable (str): The variable to make the subject.
            equation_tree (BinaryTree): The equation represented as a binary tree.

        Returns:
            BinaryTree: The rearranged equation represented as a binary tree.
        """
        rearranged_tree = BinaryTree('=') # Initialize binary tree

        # Case for (x+2)=(y+3)
        if target_variable == equation_tree._BinaryTree__left_tree._BinaryTree__left_tree.get_key():
            # Invert the operator of the left subtree to isolate the target variable
            self.__invert_operator(equation_tree._BinaryTree__left_tree)
            # Insert the target variable as the left child of the rearranged tree
            rearranged_tree.insert_left(target_variable)
            # Remove the target variable from the left subtree of the original tree
            equation_tree._BinaryTree__left_tree._BinaryTree__left_tree.set_key(None)
            # Save the left subtree of the original tree as the right subtree of the rearranged tree
            tree_no_subject = equation_tree._BinaryTree__left_tree
            rearranged_tree._BinaryTree__right_tree = tree_no_subject
            # Set the right subtree of the rearranged tree to be the right subtree of the original tree
            rearranged_tree._BinaryTree__right_tree._BinaryTree__left_tree = equation_tree._BinaryTree__right_tree

        # Case for (2+x)=(y+3)
        elif target_variable == equation_tree._BinaryTree__left_tree._BinaryTree__right_tree.get_key():
            # Invert the operator of the left subtree to isolate the target variable
            self.__invert_operator(equation_tree._BinaryTree__left_tree)
            # Insert the target variable as the left child of the rearranged tree
            rearranged_tree.insert_left(target_variable)
            # Remove the target variable from the right subtree of the original tree
            equation_tree._BinaryTree__left_tree._BinaryTree__right_tree.set_key(None)
            # Save the left subtree of the original tree as the right subtree of the rearranged tree
            tree_no_subject = equation_tree._BinaryTree__left_tree
            rearranged_tree._BinaryTree__right_tree = tree_no_subject
            # Set the right subtree of the rearranged tree to be the right subtree of the original tree
            rearranged_tree._BinaryTree__right_tree._BinaryTree__right_tree = equation_tree._BinaryTree__right_tree
            # Invert right binary tree to keep the original right tree on the left
            self.__shallow_invert_binary_tree(rearranged_tree._BinaryTree__right_tree)

        # Case for (y+3)=(x+2)
        elif target_variable == equation_tree._BinaryTree__right_tree._BinaryTree__left_tree.get_key():
            # Invert the operator of the right subtree to isolate the target variable
            self.__invert_operator(equation_tree._BinaryTree__right_tree)
            # Insert the target variable as the left child of the rearranged tree
            rearranged_tree.insert_left(target_variable)
            # Remove the target variable from the left subtree of the original tree
            equation_tree._BinaryTree__right_tree._BinaryTree__left_tree.set_key(None)
            # Save the right subtree of the original tree as the right subtree of the rearranged tree
            tree_no_subject = equation_tree._BinaryTree__right_tree
            rearranged_tree._BinaryTree__right_tree = tree_no_subject
            # Set the left subtree of the rearranged tree to be the left subtree of the original tree
            rearranged_tree._BinaryTree__right_tree._BinaryTree__left_tree = equation_tree._BinaryTree__left_tree

        # Case for (y+3)=(2+x)
        elif target_variable == equation_tree._BinaryTree__right_tree._BinaryTree__right_tree.get_key():
            # Invert the operator of the right subtree to isolate the target variable
            self.__invert_operator(equation_tree._BinaryTree__right_tree)
            # Insert the target variable as the left child of the rearranged tree
            rearranged_tree.insert_left(target_variable)
            # Remove the target variable from the right subtree of the original tree
            equation_tree._BinaryTree__right_tree._BinaryTree__right_tree.set_key(None)
            # Save the right subtree of the original tree as the right subtree of the rearranged tree
            tree_no_subject = equation_tree._BinaryTree__right_tree
            rearranged_tree._BinaryTree__right_tree = tree_no_subject
            # Set the right subtree of the rearranged tree to be the left subtree of the original tree
            rearranged_tree._BinaryTree__right_tree._BinaryTree__right_tree = equation_tree._BinaryTree__left_tree
            # Invert right binary tree to keep the original right tree on the left
            self.__shallow_invert_binary_tree(rearranged_tree._BinaryTree__right_tree)

        return rearranged_tree
    
    def __invert_operator(self, node: BinaryTree):
            """
            Inverts the operator of a given node.

            Parameters:
                node (BinaryTree): The node containing the operator to be inverted.
            """
            match node.get_key():
                case '+':
                    node.set_key('-')
                case '-':
                    node.set_key('+')
                case '*':
                    node.set_key('/')
                case '/':
                    node.set_key('*')
                case _:
                    raise ValueError(f'Only {self.__supported_operators} are supported')
    
    def __shallow_invert_binary_tree(self, node:BinaryTree):
        """
        Inverts the binary tree only at the given node.

        Parameters:
            node (BinaryTree): The node containing the binary tree to be inverted.
        """
        if (node == None): 
            return
        else:
            temp = node  
            # swap the pointers in this node
            temp = node._BinaryTree__left_tree
            node._BinaryTree__left_tree = node._BinaryTree__right_tree  
            node._BinaryTree__right_tree = temp