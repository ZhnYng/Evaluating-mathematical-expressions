from AbstractClasses import Node
from utils import BracketChecker
import re

class Statement(Node):
    def __init__(self, statement):
        statement = statement.replace(" ", "")
        var, exp = self.split_statement(statement)
        tokens = re.findall(r'\*\*|[\d.]+|\w+|[^\s\w]', exp) # Tokenize expression

        # Validating operations of expression
        operators, var_or_num = self.validate_operators(tokens)

        # Handle single values
        if len(var_or_num) == 1:
            if len(operators) == 1 and operators[0] == '-':
                exp = f'(0-{var_or_num[0]})' # Keep forrmat of expressions the same
            else:
                exp = f'({var_or_num[0]}+0)' # Keep forrmat of expressions the same
                
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

    def split_statement(self, statement):
        try:
            var, exp = statement.split('=')
        except ValueError:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")
        
        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        return var, exp
        
    def validate_operators(self, tokenized_expression):
        supported_operators = ['+', '-', '*', '/', '**']

        operators = []
        var_or_num = []
        for term in tokenized_expression:
            if term in supported_operators: # Check for supported operators
                operators.append(term)
            elif term.isalnum() or term.replace(".", "").isnumeric(): # Check for integer or float term
                var_or_num.append(term)
        
        if len(operators)+1 != len(var_or_num): # Number of operators will always be one more than the number of variables or constant/number
            if len(var_or_num) != 1 and len(operators) == 1 and operators[0] == '-':
                raise ValueError(f'Number of valid operators do not match the number of variables in {''.join(tokenized_expression)}.')

        return operators, var_or_num
    
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