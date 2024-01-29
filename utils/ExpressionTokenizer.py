class ExpressionTokenizer:
    def __init__(self):
        self.valid_operators = {'+', '-', '*', '/', '**', '(', ')'}
        self.tokens = []

    def __is_valid_operator(self, char):
        return char in self.valid_operators

    def tokenize_expression(self, expression):
        current_token = ''
        last_token = None
        paren_depth = 0  # Depth of nested parentheses
        token_count_since_last_paren = 0  # Count of tokens since last '('

        for i, char in enumerate(expression):
            if char.isspace():
                continue

            if char.isalnum() or char == '.':
                current_token += char
                last_token = char
                
            elif self.__is_valid_operator(char):
                if current_token:
                    self.tokens.append(current_token)
                    current_token = ''
                    if paren_depth > 0:
                        token_count_since_last_paren += 1

                if char == '-' and last_token == '(':
                    self.tokens.append('0')
                    token_count_since_last_paren += 1

                if char == '(':
                    paren_depth += 1
                    token_count_since_last_paren = 0
                elif char == ')' and paren_depth > 0:
                    paren_depth -= 1
                    if token_count_since_last_paren == 1:  # Only one token since last '('
                        self.tokens.extend(['+', '0'])

                if char == '*' and last_token == '*':
                    self.tokens[-1] = '**' # Handle power operation
                else:
                    self.tokens.append(char)
                last_token = char
            else:
                raise ValueError(f"Invalid character: {char}")

        if current_token:
            self.tokens.append(current_token)

        supported_operators = ['+', '-', '*', '/', '**']

        operators = []
        var_or_num = []
        for term in self.tokens:
            if term in supported_operators: # Check for supported operators
                operators.append(term)
            elif term.isalnum() or term.replace(".", "").isnumeric(): # Check for integer or float term
                var_or_num.append(term)

        if len(var_or_num) == 0:
            raise ValueError(f'Expression must have at least one number or variable')
        if len(operators)+1 != len(var_or_num): # Number of operators will always be one less than the number of variables or constant/number
            raise ValueError(f'Number of valid operators do not match the number of variables in {''.join(self.tokens)}.')
        
        if len(var_or_num) != len(operators) + 1:
            raise ValueError("Invalid expression: Operators have an invalid number of operands")

        return self.tokens
