class ExpressionTokenizer:
    def __init__(self):
        self.valid_special_chars = {'+', '-', '*', '/', '**', '(', ')'}
        self.tokens = []

    def __is_valid_special_char(self, char):
        return char in self.valid_special_chars

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
                
            elif self.__is_valid_special_char(char):
                if current_token:
                    self.tokens.append(current_token)
                    current_token = ''
                    if paren_depth > 0:
                        token_count_since_last_paren += 1

                # Handling single negative values e.g. (-3) get converted to (0-3)
                if char == '-' and last_token == '(':
                    if self.allow_exp_alter():
                        self.tokens.append('0')
                        token_count_since_last_paren += 1
                    else:
                        raise PermissionError("Expression alteration denied")

                if char == '(':
                    paren_depth += 1
                    token_count_since_last_paren = 0
                elif char == ')' and paren_depth > 0:
                    paren_depth -= 1
                    # Handling single positive values e.g. (3) get converted to (3+0)
                    if token_count_since_last_paren == 1:  # Only one token since last '('
                        if self.allow_exp_alter():
                            self.tokens.extend(['+', '0'])
                            token_count_since_last_paren += 1
                        else:
                            raise PermissionError("Expression alteration denied")

                if char == '*' and last_token == '*':
                    self.tokens[-1] = '**' # Handle power operation
                else:
                    self.tokens.append(char)
                last_token = char
            else:
                raise ValueError(f"Invalid character: {char}")

        if current_token:
            self.tokens.append(current_token)

        return self.tokens
    
    def allow_exp_alter(self):
        allow_alter = input('\nExpressions must follow operand, operator, operand format.\
                            \nBy proceeding you agree to altering the expression to this format.\
                            \nProceed?(Y/N): ').upper()
        if allow_alter == "Y":
            return True
        return False