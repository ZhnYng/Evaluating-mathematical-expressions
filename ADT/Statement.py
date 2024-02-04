from AbstractClasses import Node
from utils.ExpressionTokenizer import ExpressionTokenizer
from utils.Validation import Validation

class Statement(Node):
    def __init__(self, statement):
        # Initialize a Validation object for input validation
        self.validation = Validation()
            
        # Split the statement into variable and expression parts
        var, exp = self.split_statement(statement)

        # Tokenize the expression part using an ExpressionTokenizer object
        tokenizer = ExpressionTokenizer()
        tokens = tokenizer.tokenize_expression(exp)

        # Validate the variable name and expression tokens
        self.validation.validate_variable_name(var)  # Validate variable names
        self.validation.validate_expression(tokens)  # Validate expression
        
        super().__init__()  # Call the superclass constructor
        self.__statement = statement  # Set the statement
        self.__var = var  # Set the variable
        self.__exp = exp  # Set the expression
        self.__tokens = tokens  # Set the tokens

    # Getter and setter for statement
    def get_statement(self):
        """Returns the statement."""
        return self.__statement
    
    def set_statement(self, statement):
        """Sets the statement."""
        self.__statement = statement

    # Getter and setter for var
    def get_var(self):
        """Returns the variable."""
        return self.__var
    
    def set_var(self, var):
        """Sets the variable."""
        self.__var = var

    # Getter and setter for exp
    def get_exp(self):
        """Returns the expression."""
        return self.__exp
    
    def set_exp(self, exp):
        """Sets the expression."""
        self.__exp = exp

    # Getter and setter for tokens
    def get_tokens(self):
        """Returns the expression."""
        return self.__tokens
    
    def set_tokens(self, tokens):
        """Sets the expression."""
        self.__tokens = tokens

    # Prompt user for permission to remove spaces from the statement
    def allow_remove_spaces(self):
        allow_alter = input('\nWe found spaces in the statement you have entered.\
                            \nBy proceeding with this statement we will remove all spaces.\
                            \nProceed?(Y/N): ').upper()
        if allow_alter == "Y":
            return True
        return False

    # Split the statement into variable and expression parts
    def split_statement(self, statement):
        # Check if the statement contains spaces and prompt user for permission to remove them
        if self.validation.contains_spaces(statement):
            if self.allow_remove_spaces():
                statement = statement.replace(" ", "")
            else:
                raise PermissionError("Statement alteration denied")
        try:
            # Split the statement into variable and expression parts
            var, exp = statement.split('=')
        except ValueError:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")
        
        # Check if the statement is in the correct format
        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        return var, exp
        
    def __lt__(self, other):
        """
        Less than comparison for Statements.

        Parameters:
        - other: Another Statement object to compare with.

        Returns:
        - bool: True if the current Statement's variable is less than the other Statement's variable, False otherwise.

        Raises:
        - TypeError: If the other object is not an instance of Statement.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var < other.__var

    def __gt__(self, other):
        """
        Greater than comparison for Statements.

        Parameters:
        - other: Another Statement object to compare with.

        Returns:
        - bool: True if the current Statement's variable is greater than the other Statement's variable, False otherwise.

        Raises:
        - TypeError: If the other object is not an instance of Statement.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var > other.__var

    def __str__(self):
        """
        Get a string representation of the Statement.

        Returns:
        - str: A string representation of the Statement.
        """
        return f"{self.__statement}"

    """
    OOP Principles applied

    Encapsulation:
    The Statement class encapsulates attributes (__statement, __var, __exp, tokens) and methods 
    (split_statement, allow_remove_spaces, __lt__, __gt__, __str__) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, 
    promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the Statement class using high-level methods like get_statement(), 
    get_var(), get_exp(), set_statement(), set_var(), set_exp(), and __str__(), without needing to 
    know the internal implementation details of these methods. They are abstracted away from the 
    complexities of statement processing, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The Statement class implements comparison methods (__lt__, __gt__) to support less than and 
    greater than comparisons between Statement objects. This flexibility allows users to compare 
    statements based on their variables, promoting code flexibility and reuse.

    Modularity:
    Each method in the Statement class serves a specific purpose, promoting modularity and code 
    reusability. For example, split_statement() is responsible for parsing the input statement, 
    allow_remove_spaces() handles user interaction for removing spaces, and __str__() provides a 
    string representation of the statement. This modular design makes the class easier to understand, 
    maintain, and extend.

    """