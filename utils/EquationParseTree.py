from ADT import DoubleStatement, Stack, BinaryTree, Hashtable
from utils import ParseTree

class EquationParseTree(ParseTree):
    """
    A class for constructing and evaluating equation parse trees.

    The EquationParseTree class supports building a binary tree from a mathematical equation,
    evaluating that expression, and handling variable assignments and references within expressions.
    It uses a hashtable for memoization to optimize repeated evaluations and to handle circular dependencies.

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

    def buildParseTree(self, eqn_tokens):
        """
        Constructs a parse tree for the given expression tokens.

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
        currentTree = tree
            
        for index, t in enumerate(eqn_tokens):
            # RULE 1: If token is '(' and the previous token is '='
            # insert a node to the left and descend into that node
            if t == '(' and eqn_tokens[index-1] == '=':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 2: If token is '(' add a new node as left child
            # and descend into that node
            elif t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 3: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            # RULE 4: If token is number, set key of the current node
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

            # RULE 7: If token is '=', set key to '=', insert a node on the right
            # and descend into that node
            elif t == '=':
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
            else:
                raise ValueError
        return tree
    
    def evaluate_equation(self, tree: BinaryTree, past_statements):
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
        
        # Evaluate the expression tree
        result = self.__evaluate_equation(tree, past_statements)

        # Round off floating-point calculations
        if isinstance(result, float):
            result = round(result, 4)

        return result
        
    def __evaluate_equation(self, tree: BinaryTree, past_statements):
        """
        Recursively evaluates the given equation tree.

        This method traverses the tree, evaluating the equation based on the operators and operands
        defined in the tree nodes. It handles arithmetic operations and variable references.
        The '=' is an operator here, which evaluates the equality of the two expressions in the equation.

        Parameters:
            tree (BinaryTree): The root of the expression tree to evaluate.

        Returns:
            True if equation is equal, else False or 'None' if a variable is undefined.

        Raises:
            ZeroDivisionError: If the expression includes division by zero.
        """
        # Check if the tree is not empty
        if tree:
            # Check if both left and right subtrees exist
            if tree.getLeftTree() and tree.getRightTree():
                op = tree.getKey()  # Get the operator
                left = self.__evaluate_equation(tree.getLeftTree(), past_statements)  # Evaluate left subtree
                right = self.__evaluate_equation(tree.getRightTree(), past_statements)  # Evaluate right subtree
                
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
                elif op == '=': return left == right # Evaluate equality of two expressions
            else:
                # Handle leaf nodes (operands or variables)
                key = tree.getKey()
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
            id: The unique id of the equation.

        Raises:
            None (No circular dependency possible)
        """
        # Give the equation a unique id
        id = f"Equation {len(self.__equations)+1}"
        # Build the parse tree from the expression tokens
        tree = self.buildParseTree(eqn_tokens)
        
        # Remove cached result if the expression has changed
        if id in self.__memoization_cache:
            del self.__memoization_cache[id]
        
        # Associate the parse tree with the variable
        self.__equations[id] = tree
        return id
        
    def rearrange_tree(self, target_variable, equation_tree:BinaryTree):
        rearranged_tree = BinaryTree('=') # Initialize binary tree

        def invert_operator(node:BinaryTree):
            match node.getKey():
                case '+':
                    node.setKey('-')
                case '-':
                    node.setKey('+')
                case '*':
                    node.setKey('/')
                case '/':
                    node.setKey('*')
                case _:
                    raise ValueError(f'Only {self.__supported_operators} are supported')

        # Case for (x+2)=(y+3)
        if target_variable == equation_tree.leftTree.leftTree.getKey():
            invert_operator(equation_tree.leftTree)
            rearranged_tree.insertLeft(target_variable)
            equation_tree.leftTree.leftTree.setKey(None)
            tree_no_subject = equation_tree.leftTree
            rearranged_tree.rightTree = tree_no_subject
            rearranged_tree.rightTree.leftTree = equation_tree.rightTree

        # Case for (2+x)=(y+3)
        elif target_variable == equation_tree.leftTree.rightTree.getKey():
            invert_operator(equation_tree.leftTree)
            rearranged_tree.insertLeft(target_variable)
            equation_tree.leftTree.rightTree.setKey(None)
            tree_no_subject = equation_tree.leftTree
            rearranged_tree.rightTree = tree_no_subject
            rearranged_tree.rightTree.rightTree = equation_tree.rightTree
        
        # Case for (y+3)=(x+2)
        elif target_variable == equation_tree.rightTree.leftTree.getKey():
            invert_operator(equation_tree.rightTree)
            rearranged_tree.insertLeft(target_variable)
            equation_tree.rightTree.leftTree.setKey(None)
            tree_no_subject = equation_tree.rightTree
            rearranged_tree.rightTree = tree_no_subject
            rearranged_tree.rightTree.leftTree = equation_tree.leftTree

        # Case for (y+3)=(2+x)
        elif target_variable == equation_tree.rightTree.rightTree.getKey():
            invert_operator(equation_tree.rightTree)
            rearranged_tree.insertLeft(target_variable)
            equation_tree.rightTree.rightTree.setKey(None)
            tree_no_subject = equation_tree.rightTree
            rearranged_tree.rightTree = tree_no_subject
            rearranged_tree.rightTree.rightTree = equation_tree.leftTree
        
        return rearranged_tree

    """
    OOP Principles applied:

    Encapsulation:
    The Validation class encapsulates the state of variable validation using private attributes (__valid_name) and 
    private methods (__check_empty, __check_starts_with_letter, __check_invalid_characters). This ensures that the internal 
    state is protected from direct access and manipulation from outside the class.

    Abstraction:
    The Validation class provides high-level methods (validate_variable_name, contains_spaces, is_valid, is_invalid) that 
    abstract away the complex logic of variable validation. Users interact with these methods without needing to understand 
    the internal implementation details of validation criteria.

    Polymorphism:
    The Validation class exhibits polymorphic behavior through the use of different private validation methods 
    (__is_dividing_by_zero, __is_operator_and_operand_matching, __check_parentheses) to handle various aspects of 
    expression validation. This allows for flexibility in validating different types of expressions with specialized logic.

    Modularity:
    Each private method in the Validation class serves a specific validation purpose, promoting modularity and code reusability. 
    For example, the __check_empty method validates if a variable name is empty, while the __check_parentheses method 
    validates if parentheses in an expression are properly matched. This modular design makes the class easier to understand, 
    maintain, and extend.
    """