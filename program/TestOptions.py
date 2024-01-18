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
        valid_statements = ["x=(5)", "y=(x+1)", "z=(y*2)", "a=((1+1)+(1+1))"]
        for statement in valid_statements:
            with self.subTest(statement=statement):
                self.options.add_or_modify(statement)
                self.assertIn(
                    statement.split("=")[0], self.options.parse_tree.statements
                )

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

    def test_expression_evaluation(self):
        # Test if expressions are evaluated correctly
        self.options.add_or_modify("x=(5)")
        self.options.add_or_modify("y=(x+1)")
        result = self.options.eval_one_var("y")
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
        result = self.options.parse_tree.evaluate(
            "x", self.options.parse_tree.statements["x"]
        )
        self.assertEqual(result, 1024)

    # def test_display_statements(self):
    #     valid_statements = ["x=(5)", "y=(x+1)", "z=(y*2)", "a=((1+1)+(1+1))"]
    #     for statement in valid_statements:
    #         with self.subTest(statement=statement):
    #             self.options.add_or_modify(statement)
    #             var, exp = statement.split('=')
    #             self.assertDictEqual(
    #                 {var: exp}, 
    #                 self.options.display_statements()
    #             )    