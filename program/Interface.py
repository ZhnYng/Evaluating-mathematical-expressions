# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# This class represents the user interface/GUI for the 
# Evaluating & Sorting Assignment Statements (using parse trees) application.
# It provides various options for evaluating solutions, altering variables, and flexible evaluations.
#
# -----------------------------------------------------
#
# Author    : Ashley Bai
# StudentID : 2237871
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : Interface.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
from utils import Validation

class Interface:
    """
    This class represents the user interface/GUI for the 
    Evaluating & Sorting Assignment Statements (using parse trees) application.
    It provides various options for evaluating solutions, altering variables, and flexible evaluations.
    """

    def __init__(self):
        """
        Initializes the Interface class.
        """
        self.validation = Validation()

    def banner(self):
        """
        Prints the introductory banner for the application.
        """
        print('*'*65)
        print('* ST1507 DSAA: Evaluating & Sorting Assignment Statements ', ' '*4, '*')
        print('*', '-'*61, '*')
        print('*', ' '*61, '*')
        print('* - Done by: Lim Zhen Yang (2214506) & Ashley Bai (2237871)', ' '*3, '*')
        print('* - Class DAAA/FT/2B04', ' '*40, '*')
        print('*', ' '*61, '*')
        print('*'*65, end='\n\n\n')

    def pause(self):
        """
        Pauses the program execution and waits for user input to continue.
        """
        input("\nPress enter key, to continue...\n")

    def error_msg(self, error_msg):
        """
        Format for printing out error messages within an option.
        """
        print(f'\nAn error occurred: {error_msg}\n(Press Ctrl+C to exit)\n')

    # Option 1
    def option1(self, add_or_modify):
        """
        Executes the first option in the menu: add or modify an assignment statement.

        Parameters:
        - add_or_modify: Function to add or modify an assignment statement.
        """
        while True:
            try:
                statement = input(f"Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
                add_or_modify(statement)
                self.pause()
                break
            except Exception as e:
                self.error_msg(e)
        
        
            
    # Option 2
    def option2(self, display_statements):
        """
        Executes the second option in the menu: display current assignment statements.

        Parameters:
        - display_statements: Function to display current assignment statements.
        """
        statement_and_answers = display_statements()
        if statement_and_answers:
            print(f"\nCURRENT ASSIGNMENTS:\n{'*'*20}")
        for statement, answer in statement_and_answers.items():
            print(f"{statement}=> {answer}")
        self.pause()
        
    # Option 3
    def option3(self, eval_one_var):
        """
        Executes the third option in the menu: evaluate an individual variable.

        Parameters:
        - eval_one_var: Function to evaluate an individual variable.
        """
        while True:
            try:
                # Get user input for the variable to be evaluated
                variable = input("Please enter the variable you want to evaluate:\n")
                # Evaluate the specified variable using the eval_one_var function
                expression_tree_str, result = eval_one_var(variable)

                # Print result
                print('\nExpression Tree:')
                print(expression_tree_str, end='')
                print(f"Value for variable \"{variable}\" is {result}\n")

                self.pause()
                break
            except Exception as e:
                self.error_msg(e)

    # Option 4
    def option4(self, read_from_file):
        """
        Executes the fourth option in the menu: read and evaluate assignment statements from a file.

        Parameters:
        - read_from_file: Function to read and evaluate assignment statements from a file.
        """
        while True:
            try:
                # Get user input for input file
                file = input("Please enter input file: ")
                
                # Call the read_from_file method to read and evaluate statements
                assignments_dict = read_from_file(file)

                print("\nCURRENT ASSIGNMENTS:")
                print("****************************")

                # Sort the assignments alphabetically
                for assignment, value in sorted(assignments_dict.items()):
                    print(f'{assignment} => {value}')
                    
                self.pause()
                break
            except Exception as e:
                self.error_msg(e)
                
    # Option 5 
    def option5(self, sorting_expressions):
        """
        Executes the fifth option in the menu: sort expressions and store the sorted assignment statements in an output file.

        Parameters:
        - sorting_expressions: Function to sort expressions and store the sorted assignment statements in an output file.
        """
        while True:
            try:
                # Get user input for output file
                file = input("Please enter output file: ")
                
                # Call the sorting expression function 
                sorting_expressions(file)
                
                print('\n')
                break
            except Exception as e:
                self.error_msg(e)

    # Option 6
    def option6(self, eval_equation):
        """
        Executes the sixth option in the menu: evaluate if two expressions are equal.

        Parameters:
        - eval_equation: Function to evaluate if two expressions are equal.
        """
        while True:
            try:
                eqn = input('Enter the equation you want to equate:\nFor example, (x+2)=(y+3)\n')
                if eval_equation(eqn) == 'None':
                    print('\nThe equation is unknown')
                elif eval_equation(eqn):
                    print('\nThe equation is equal')
                else:
                    print('\nThe equation is not equal')

                self.pause()
                break
            except Exception as e:
                self.error_msg(e)

    # Option 7
    def option7(self, solve_equation):
        """
        Executes the seventh option in the menu: solve an equation for a specified variable.

        Parameters:
        - solve_equation: Function to solve an equation for a specified variable.
        """
        while True:
            try:
                eqn = input('Enter the equation you want to solve:\nFor example, (x+2)=(y+3)\n')
                subject = input('\nEnter the subject of the equation to solve for: ')
                print('\n' + solve_equation(eqn, subject))

                self.pause()
                break
            except Exception as e:
                self.error_msg(e)