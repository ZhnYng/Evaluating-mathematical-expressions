# from program import TestOptions
# import unittest
# if __name__ == '__main__':
#     unittest.main()

from program import Interface, Options
interface = Interface()
options = Options()

options.read_from_file('fruits.txt')
options.sorting_expressions('fruits_sorted.txt')
# print(options.display_statements())

# # Define a function to start the program
# def start_program():
#     # Display the program banner
#     interface.banner()
#     #Main program loop
#     choice = ''
#     while choice != '8':
#         # Prompt the user for their choice
#         choice = input("Please select your choice: ('1','2','3','4','5','6'):\n"
#                        '    1. Add/Modify assignment statement\n'
#                        '    2. Display current assignment statements\n'
#                        '    3. Evaluate a single variable\n'
#                        '    4. Read assignment statements from file\n'
#                        '    5. Sort assignment statements\n'
#                        '    6. Exit\n'
#                        'Enter choice: ')
#         # try:
#         # Use a match statement to handle user choices
#         match choice:
#             case '1':
#                 interface.option1(options.add_or_modify)
#                 pass
#             case '2':
#                 interface.option2(options.display_statements)
#                 pass
#             case '3':
#                 interface.option3(options.eval_one_var)
#                 pass
#             case '4':
#                 interface.option4(options.read_from_file)
#                 pass
#             case '5':
#                 interface.option5(options.sorting_expressions)
#                 pass
#             case '6':
#                 print("\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter!")
#                 break
#         # except Exception as e:
#         #     # Handle exceptions and display an error message
#         #     print(f'\n{e}')
#     else:
#         # Display a goodbye message when the program exits
#         print('\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer')

# # Entry point of the program
# if __name__ == '__main__':
#     start_program()