from program import TestOptions
import unittest
if __name__ == '__main__':
    unittest.main()

# from program import Interface, Options

# interface = Interface()
# options = Options()

# Backend/Options test cases
# options.add_or_modify('Apple=(2+(4*5))')
# options.add_or_modify('Pear=(Apple*3)')
# options.add_or_modify('Mango=((Apple+(Durian+(Pear*(Blueberry*(Coconut/Strawberry)))))/2)')
# print(options.display_statements())
# print(options.eval_one_var('Pear'))
# (options.read_from_file('fruits.txt'))
# print(options.sorting_expressions('fruits_sorted.txt'))
# options.add_or_modify("x=(5)")
# options.add_or_modify("y=(x+1)")
# print(options.eval_one_var('y'))

# options.add_or_modify("pine_apple=(y+1)")
# options.add_or_modify("y=(x+2)")
# print(options.display_statements())