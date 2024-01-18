# Import necessary modules and classes
from program import Interface, Options

# Create an instance of the Interface and Options classes
interface = Interface()
options = Options()

# Backend/Options test cases
# options.add_or_modify('Apple=(2+(4*5))')
# options.add_or_modify('Pear=(Apple*3)')
# options.add_or_modify('Mango=((Apple+(Durian+(Pear*(Blueberry*(Coconut/Strawberry)))))/2)')
# (options.read_from_file('fruits.txt'))
# print(options.sorting_expressions('fruits_sorted.txt'))

# Define a function to start the program
def start_program():
    # Display the program banner
    interface.banner()
    #Main program loop
    choice = ''
    while choice != '8':
        # Prompt the user for their choice
        choice = input("Please select your choice: ('1','2','3','4','5','6'):\n"
                       '\t1. Add/Modify assignment statement\n'
                       '\t2. Display current assignment statements\n'
                       '\t3. Evaluate a single variable\n'
                       '\t4. Read assignment statements from file\n'
                       '\t5. Sort assignment statements\n'
                       '\t6. Exit\n'
                       'Enter choice: ')
        # try:
        # Use a match statement to handle user choices
        match choice:
            case '1':
                interface.option1(options.add_or_modify)
                pass
            case '2':
                interface.option2(options.display_statements)
                pass
            case '3':
                interface.option3(options.eval_one_var)
                pass
            case '4':
                # interface.option4(options.infer_caesar_key_from_file, options.file_cryptography)
                pass
            case '5':
                # interface.option5(options.analyze_sort_encrypted_files)
                pass
            case '6':
                # interface.option6(options.craft_encryption)
                pass
            case '7':
                # interface.option7(options.multi_cryptography)
                pass
        # except Exception as e:
        #     # Handle exceptions and display an error message
        #     print(f'\n{e}')
    else:
        # Display a goodbye message when the program exits
        print('\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer')

# Entry point of the program
if __name__ == '__main__':
    start_program()