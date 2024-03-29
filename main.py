# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Application entry point
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : main.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
from program import Interface, Options
interface = Interface()
options = Options()

def handle_menu():
    choice = ''
    while choice != '10':
        try:
            # Mark that the user is now in the main menu
            in_main_menu = True

            # Display the menu and prompt for user input
            choice = input(
                "\nPlease select your choice: ('1','2','3','4','5','6','7','8','9','10'):\n"
                '    1. Add/Modify assignment statement\n'
                '    2. Display current assignment statements\n'
                '    3. Evaluate a single variable\n'
                '    4. Read assignment statements from file\n'
                '    5. Sort assignment statements\n'
                '    6. Equate an equation\n'
                '    7. Solve for a subject in an equation\n'
                '    8. Display history log\n'
                '    9. Visualize parse trees\n'
                '    10. Exit\n'
                'Enter choice: '
            )

            # Use a match statement to handle user choices
            in_main_menu = False
            match choice:
                case '1':
                    interface.option1(options.add_or_modify)
                case '2':
                    interface.option2(options.display_statements)
                case '3':
                    interface.option3(options.eval_one_var)
                case '4':
                    interface.option4(options.read_from_file)
                case '5':
                    interface.option5(options.sorting_expressions)
                case '6':
                    interface.option6(options.eval_equation)
                case '7':
                    interface.option7(options.make_subject_of_eqn)
                case '8':
                    options.displayHistory()
                case '9':
                    options.visualize_parse_tree()
                case '10':
                    print('\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter')
                    return  # Exit function when user chooses '10'
        except Exception as e:
            print(f'\nAn error occurred: {e}')
        except KeyboardInterrupt:
            if in_main_menu:  # Check if the user is in the main menu before printing the message
                print("\n\nUse menu choice '10' to exit.")
            else:
                print("\n")

# Define a function to start the program
def start_program():
    # Display the program banner
    interface.banner()
    # Call the function to handle the menu and user choices
    handle_menu()

# Entry point of the program
if __name__ == '__main__':
    start_program()