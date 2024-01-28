from AbstractClasses import Node
from utils import BracketChecker
import re

class Statement(Node):
    def __init__(self, statement):
        statement = statement.replace(" ", "")
        try:
            var, exp = statement.split('=')
        except ValueError:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        tokens = re.findall(r'\*\*|[\d.]+|\w+|[^\s\w]', exp)

        # Validating operation of expression
        supported_operators = ['+', '-', '*', '/', '**']

        no_of_operators = 0
        no_of_var_or_num = 0
        for char in tokens:
            if char in supported_operators:
                no_of_operators += 1
            if char.isalnum() or char.replace(".", "").isnumeric():
                no_of_var_or_num += 1
        if no_of_operators+1 != no_of_var_or_num:
            raise ValueError(f'Number of valid operators do not match the number of variables in {statement}.')

        supported = any(operator in tokens for operator in supported_operators)

        # Handle single values
        if not supported:
            # Strip brackets to check validity of expression
            def strip_all_brackets(expression):
                while '(' in expression:
                    start = expression.rfind('(')
                    end = expression.find(')', start)
                    if start != -1 and end != -1:
                        expression = expression[:start] + expression[start+1:end] + expression[end+1:]
                return expression
            temp_exp = strip_all_brackets(exp)
            if any(not c.isalnum() for c in temp_exp): # If expression contains any special characters 
                if not temp_exp.isalpha(): # Test for expression containing alphabet
                    raise ValueError(f"Expression must have at least one variable or number")
                elif not temp_exp.isnumeric() or not temp_exp.replace(".", "").isnumeric(): # Test for expression containing number/float
                    raise ValueError(f"Invalid expression format. Only {supported_operators} are accepted.")
            else:
                exp = f'({temp_exp}+0)' # Keep format of expressions consistent

        # Function to handle negative numbers
        def handle_negative_numbers(expression):
            # Replace standalone negative numbers (e.g., (-3) becomes (0-3))
            return re.sub(r'(?<=\()\s*-(?=\d)', '0-', expression)
        
        exp = handle_negative_numbers(exp)

        # Expression must be fully parenthesized
        bracket_checker = BracketChecker()
        is_fully_paren = bracket_checker.check(tokens)
        if not is_fully_paren:
            raise ValueError('Expressions must be fully parenthesized')

        super().__init__()
        self.__statement = statement
        self.__var = var
        self.__exp = exp

    @property
    def statement(self):
        """Returns the statement."""
        return self.__statement
    
    @property
    def var(self):
        """Returns the statement."""
        return self.__var
    
    @property
    def exp(self):
        """Returns the statement."""
        return self.__exp

    @statement.setter
    def statement(self, statement):
        """Sets the statement."""
        self.__statement = statement

    @var.setter
    def var(self, var):
        """Sets the statement."""
        self.__statement = var

    @exp.setter
    def exp(self, exp):
        """Sets the statement."""
        self.__statement = exp

    def __lt__(self, other):
        """
        Less than comparison for Files.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var < other.__var

    def __gt__(self, other):
        """
        Greater than comparison for Files.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var > other.__var
    
    def __str__(self):
        return f"{self.__statement}"