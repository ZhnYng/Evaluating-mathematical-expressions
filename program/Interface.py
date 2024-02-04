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

    # Option 1
    def option1(self, add_or_modify):
        """
        Executes the first option in the menu: add or modify an assignment statement.

        Parameters:
        - add_or_modify: Function to add or modify an assignment statement.
        """
        statement = input(f"Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
        add_or_modify(statement)
        self.pause()

    # Option 2
    def option2(self, display_statements):
        """
        Executes the second option in the menu: display current assignment statements.

        Parameters:
        - display_statements: Function to display current assignment statements.
        """
        print(f"\nCURRENT ASSIGNMENTS:\n{'*'*20}")
        statement_and_answers = display_statements()
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
        # Get user input for the variable to be evaluated
        variable = input("Please enter the variable you want to evaluate:\n")
        # Evaluate the specified variable using the eval_one_var function
        expression_tree_str, result = eval_one_var(variable)

        # Print result
        print('\nExpression Tree:')
        print(expression_tree_str, end='')
        print(f"Value for variable \"{variable}\" is {result}\n")

        # Print additional message
        self.pause()
        
        
    # Option 4
    def option4(self, read_from_file):
        """
        Executes the fourth option in the menu: read and evaluate assignment statements from a file.

        Parameters:
        - read_from_file: Function to read and evaluate assignment statements from a file.
        """
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
        
    # Option 5 
    def option5(self, sorting_expressions):
        """
        Executes the fifth option in the menu: sort expressions and store the sorted assignment statements in an output file.

        Parameters:
        - sorting_expressions: Function to sort expressions and store the sorted assignment statements in an output file.
        """
        # Get user input for output file
        file = input("Please enter output file: ")
        
        # Call the sorting expression function 
        sorting_expressions(file)
        
        print('\n')
    def option6(self, display_parse_tree):
        var = input("Please enter the variable you want to visualize:\n")
        display_parse_tree(var)
        self.pause()