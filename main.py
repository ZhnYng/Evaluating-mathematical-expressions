from program import TestOptions
import unittest
if __name__ == '__main__':
    unittest.main()

# from program import Interface, Options
# interface = Interface()
# options = Options()

# def handle_menu():
#     choice = ''
#     while choice != '6':
#         try:
#             # Mark that the user is now in the main menu
#             in_main_menu = True

#             # Display the menu and prompt for user input
#             choice = input(
#                 "Please select your choice: ('1','2','3','4','5','6'):\n"
#                 '    1. Add/Modify assignment statement\n'
#                 '    2. Display current assignment statements\n'
#                 '    3. Evaluate a single variable\n'
#                 '    4. Read assignment statements from file\n'
#                 '    5. Sort assignment statements\n'
#                 '    6. Exit\n'
#                 'Enter choice: '
#             )

#             # Use a match statement to handle user choices
#             in_main_menu = False
#             match choice:
#                 case '1':
#                     interface.option1(options.add_or_modify)
#                 case '2':
#                     interface.option2(options.display_statements)
#                 case '3':
#                     interface.option3(options.eval_one_var)
#                 case '4':
#                     interface.option4(options.read_from_file)
#                 case '5':
#                     interface.option5(options.sorting_expressions)
#                 case '6':
#                     print('\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter')
#                     return  # Exit function when user chooses '6'
#         # except Exception as e:
#         #     print(f'\nAn error occurred: {e}')
#         except KeyboardInterrupt:
#             if in_main_menu:  # Check if the user is in the main menu before printing the message
#                 print("\n\nUse menu choice '6' to exit.")
#             else:
#                 print("\n")

# # Define a function to start the program
# def start_program():
#     # Display the program banner
#     interface.banner()
#     # Call the function to handle the menu and user choices
#     handle_menu()


# # Entry point of the program
# if __name__ == '__main__':
#     start_program()