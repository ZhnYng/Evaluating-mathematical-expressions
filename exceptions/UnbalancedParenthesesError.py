class UnbalancedParenthesesError(Exception):
    def __init__(self, message="Unbalanced parentheses detected"):
        self.message = message
        super().__init__(self.message)