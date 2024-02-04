import unittest
from program import Options  # Replace with actual module name


class TestOptions(unittest.TestCase):
    """
    This setup covers a wide range of scenarios:

    Valid Statements: Ensures correctly formatted statements are added.
    Invalid Statements: Checks for statements that should raise UnbalancedParenthesesError.
    Duplicate Statements: Assumes that a KeyError (or a similar exception) is raised for duplicate variable names.
    Circular Dependencies: Tests for circular dependencies in the expression trees.
    Expression Evaluation: Validates the correct evaluation of expressions.
    Edge Cases: Includes tests for empty statements and very long expressions.
    """

    def setUp(self):
        # Setup for each test
        self.options = Options()

    def test_valid_statements(self):
        # Test adding valid statements
        valid_statements = [
            "x=(5)",
            "y=(x+1)",
            "z=(y*2)",
            "a=((1+1)+(1+1))",
            "b=(a*3)",
            "c=(b-2)",
            "d=((c*2)+5)",
            "e=(d/2)",
            "f=(e+3)",
            "g=(f*2)",
            "h=((g-1)/2)",
            "i=(h**2)",
            "z=((-3)*5)",
            "x=(0.1+0.2)",
        ]
        answers = [5, 6, 12, 4, 12, 10, 25, 12.5, 15.5, 31, 15, 225, -15, 0.3]

        for statement, answer in zip(valid_statements, answers):
            with self.subTest(statement=statement):
                self.options.add_or_modify(statement)
                self.assertIn(
                    statement.split("=")[0], self.options.get_parse_tree().get_statements()
                )
                _, result = self.options.eval_one_var(statement.split("=")[0])
                self.assertEqual(result, answer)

    def test_invalid_statements(self):
        # Test adding invalid statements, should raise exceptions
        invalid_statements = [
            "x=5)",
            "y=(x+1",
            "=5",
            "x=5+2",
            "x=(5+2",
            "x=(2+2+2+2+2)",
            "x=(2%2)",
            "x=(2+1)+(2+1)",
            "x=(2+1), (2+1)",
            "x=5 + 2",
            "x = (2 + 2) * (3 - 1)",
            "x=(5!)",
            "x=(5e6+1.23e-4)",
            "x=(**)",
            "x=(*)",
            "x=(/)",
            "x=/",
            "x=((a*b)+)",
            "a=(1+2)3",
            "a=()",
            "a=(2*4)$",
            "a=(1+3)+++",
            "a=(1+3)123",
            "a=((1+4))",
        ]
        for statement in invalid_statements:
            with self.subTest(statement=statement):
                with self.assertRaises(ValueError):
                    self.options.add_or_modify(statement)

    def test_circular_dependencies(self):
        # Test for circular dependencies in expressions
        self.options.add_or_modify("x=(y+1)")
        self.options.add_or_modify("y=(z+2)")
        with self.assertRaises(ValueError):
            self.options.add_or_modify("z=(x+3)")

    def test_simple_circular_dependencies(self):
        self.options.add_or_modify("a=(b+1)")
        with self.assertRaises(ValueError):
            self.options.add_or_modify("b=(a+2)")

    def test_multiple_circular_dependencies(self):
        self.options.add_or_modify("p=(q+1)")
        self.options.add_or_modify("q=(r+2)")
        self.options.add_or_modify("r=(s+3)")
        with self.assertRaises(ValueError):
            self.options.add_or_modify("s=(p+4)")

    def test_expression_evaluation(self):
        # Test if expressions are evaluated correctly
        self.options.add_or_modify("x=(5)")
        self.options.add_or_modify("y=(x+1)")
        expression_tree_str, result = self.options.eval_one_var("y")
        self.assertEqual(result, 6)

    def test_edge_cases(self):
        # Test edge cases
        # Example: Empty statement
        with self.assertRaises(ValueError):
            self.options.add_or_modify("")

        # Very long expression
        def long_exp(repetitions, exp):
            if repetitions <= 0:
                exp = f"x={exp}"
                return exp

            exp = f"({exp}+{exp})"
            return long_exp(repetitions - 1, exp)

        long_expr = long_exp(10, 1)
        self.options.add_or_modify(long_expr)
        result = self.options.get_parse_tree().evaluate(
            "x", self.options.get_parse_tree().get_statements()["x"]
        )
        self.assertEqual(result, 1024)

    def test_division_by_zero(self):
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.options.add_or_modify("x=(1/0)")

    def test_valid_variable_naming_syntax(self):
        # Test valid Python variable naming syntax requirements
        valid_variable_names = [
            "variableName",
            "anotherVariable",
            "myVar123",
            "privateVar",
        ]

        for variable_name in valid_variable_names:
            with self.subTest(variable_name=variable_name):
                statement = f"{variable_name}=(5)"
                self.options.add_or_modify(statement)
                self.assertIn(variable_name, self.options.get_parse_tree().get_statements())

    def test_invalid_variable_naming_syntax(self):
        # Test invalid Python variable naming syntax requirements
        invalid_variable_names = [
            ("123Invalid", "Variable name must start with a letter."),
            ("with spaces", 'Variable can only contain alphanumeric characters.'),
            ("Special-Char", 'Variable can only contain alphanumeric characters.'),
            ("1variable", "Variable name must start with a letter."),
            ("123", "Variable name must start with a letter."),  # Empty variable name
            ("a!", 'Variable can only contain alphanumeric characters.'),  # Special character
            ("my variable", 'Variable can only contain alphanumeric characters.'),  # Space
            ("@var", "Variable name must start with a letter."),  # Special character
            ("var$", 'Variable can only contain alphanumeric characters.'),  # Special character
        ]

        for variable_name, expected_error_message in invalid_variable_names:
            with self.subTest(variable_name=variable_name):
                statement = f"{variable_name}=(5)"
                with self.assertRaises(ValueError) as context:
                    self.options.add_or_modify(statement)
                
                # Check if the actual error message contains the expected error message
                self.assertIn(expected_error_message, str(context.exception))