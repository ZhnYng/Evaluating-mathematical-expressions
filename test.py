from utils.EquationParseTree import EquationParseTree

# Example usage
equation = "(x+2)=(3+y)"
# target = 'x'

eqn_parse_tree = EquationParseTree()
tree = eqn_parse_tree.buildParseTree(equation)
print(eqn_parse_tree.rearrange_tree('x', tree))
# rearranged_tree = rearrange_tree_for_target(tree, target)
# result_equation = tree_to_equation(rearranged_tree)
# print(result_equation)
