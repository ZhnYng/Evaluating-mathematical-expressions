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

        return self.tokens
