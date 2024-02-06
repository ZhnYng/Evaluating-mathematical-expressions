from AbstractClasses import Node
from utils.ExpressionTokenizer import ExpressionTokenizer
from utils.Validation import Validation

class Equation(Node):
    def __init__(self, equation):
        # Initialize a Validation object for input validation
        self.validation = Validation()
            
        # Split the equation into variable and expression parts
        exp1, exp2 = self.split_equation(equation)

        # Tokenize the expression part using an ExpressionTokenizer object
        tokenizer = ExpressionTokenizer()
        tokens1 = tokenizer.tokenize_expression(exp1)
        tokens2 = tokenizer.tokenize_expression(exp2)
        eqn_tokens = [*tokens1, '=', *tokens2]

        # Validate the variable name and expression tokens
        # self.validation.validate_variable_name(var)  # Validate variable names
        # self.validation.validate_expression(tokens)  # Validate expression
        
        super().__init__()  # Call the superclass constructor
        self.__equation = equation  # Set the equation
        self.__exp1 = exp1  # Set the variable
        self.__exp2 = exp2  # Set the expression
        self.__eqn_tokens = eqn_tokens  # Set the tokens

    # Getter and setter for equation
    def get_equation(self):
        """Returns the equation."""
        return self.__equation
    
    def set_equation(self, equation):
        """Sets the equation."""
        self.__equation = equation

    # Getter and setter for var
    def get_exp1(self):
        """Returns the variable."""
        return self.__var
    
    def set_exp1(self, var):
        """Sets the variable."""
        self.__var = var

    # Getter and setter for exp
    def get_exp2(self):
        """Returns the expression."""
        return self.__exp
    
    def set_exp2(self, exp):
        """Sets the expression."""
        self.__exp = exp

    # Getter and setter for tokens
    def get_tokens(self):
        """Returns the expression."""
        return self.__eqn_tokens
    
    def set_tokens(self, tokens):
        """Sets the expression."""
        self.__eqn_tokens = tokens

    # Prompt user for permission to remove spaces from the equation
    def allow_remove_spaces(self):
        allow_alter = input('\nWe found spaces in the equation you have entered.\
                            \nBy proceeding with this equation we will remove all spaces.\
                            \nProceed?(Y/N): ').upper()
        if allow_alter == "Y":
            return True
        return False

    # Split the equation into variable and expression parts
    def split_equation(self, equation):
        # Check if the equation contains spaces and prompt user for permission to remove them
        if self.validation.contains_spaces(equation):
            if self.allow_remove_spaces():
                equation = equation.replace(" ", "")
            else:
                raise PermissionError("Equation alteration denied")
        try:
            # Split the equation into variable and expression parts
            var, exp = equation.split('=')
        except ValueError:
            raise ValueError(f"Invalid equation format in {equation}. It should be in the form 'var = exp'")
        
        # Check if the equation is in the correct format
        if '=' not in equation or equation.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid equation format in {equation}. It should be in the form 'var = exp'")

        return var, exp
        
    def __lt__(self, other):
        """
        Less than comparison for Statements.

        Parameters:
        - other: Another Equation object to compare with.

        Returns:
        - bool: True if the current Equation's variable is less than the other Equation's variable, False otherwise.

        Raises:
        - TypeError: If the other object is not an instance of Equation.
        """
        if not isinstance(other, Equation):
            raise TypeError("Comparison not supported between instances of 'Equation' and other types")
        return self.__var < other.__var

    def __gt__(self, other):
        """
        Greater than comparison for Statements.

        Parameters:
        - other: Another Equation object to compare with.

        Returns:
        - bool: True if the current Equation's variable is greater than the other Equation's variable, False otherwise.

        Raises:
        - TypeError: If the other object is not an instance of Equation.
        """
        if not isinstance(other, Equation):
            raise TypeError("Comparison not supported between instances of 'Equation' and other types")
        return self.__var > other.__var

    def __str__(self):
        """
        Get a string representation of the Equation.

        Returns:
        - str: A string representation of the Equation.
        """
        return f"{self.__equation}"

    """
    OOP Principles applied

    Encapsulation:
    The Equation class encapsulates attributes (__equation, __var, __exp, tokens) and methods 
    (split_equation, allow_remove_spaces, __lt__, __gt__, __str__) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, 
    promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the Equation class using high-level methods like get_equation(), 
    get_var(), get_exp(), set_equation(), set_var(), set_exp(), and __str__(), without needing to 
    know the internal implementation details of these methods. They are abstracted away from the 
    complexities of equation processing, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The Equation class implements comparison methods (__lt__, __gt__) to support less than and 
    greater than comparisons between Equation objects. This flexibility allows users to compare 
    equations based on their variables, promoting code flexibility and reuse.

    Modularity:
    Each method in the Equation class serves a specific purpose, promoting modularity and code 
    reusability. For example, split_equation() is responsible for parsing the input equation, 
    allow_remove_spaces() handles user interaction for removing spaces, and __str__() provides a 
    string representation of the equation. This modular design makes the class easier to understand, 
    maintain, and extend.

    """