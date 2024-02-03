from AbstractClasses import Node
from utils.ExpressionTokenizer import ExpressionTokenizer
from utils.Validation import Validation

class Statement(Node):
    def __init__(self, statement):
        self.validation = Validation()
            
        var, exp = self.split_statement(statement)

        tokenizer = ExpressionTokenizer()
        tokens = tokenizer.tokenize_expression(exp)

        self.validation.validate_variable_name(var) # Validate variable names
        self.validation.validate_expression(tokens) # Validate expression
        
        super().__init__()
        self.__statement = statement
        self.__var = var
        self.__exp = exp
        self.tokens = tokens

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

    def allow_remove_spaces(self):
        allow_alter = input('\nWe found spaces in the statement you have entered.\
                            \nBy proceeding with this statement we will remove all spaces.\
                            \nProceed?(Y/N): ').upper()
        if allow_alter == "Y":
            return True
        return False

    def split_statement(self, statement):
        if self.validation.contains_spaces(statement):
            if self.allow_remove_spaces():
                statement = statement.replace(" ", "")
            else:
                raise PermissionError("Statement alteration denied")
        try:
            var, exp = statement.split('=')
        except ValueError:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")
        
        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        return var, exp
        
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