from criteria_constraint import criteria_constraint
from pareto import pareto
from weighing_combining_criteria import weigh_combine_criteria
from input import W, CANDIDATES


def main():
	print('Criteria Constraint Method:')
	criteria_constraint(W, CANDIDATES, 'character', aim_max = True)
	print()

	print('Pareto Set Method:')
	pareto(W, CANDIDATES, ['character', 'appearance'], aim_max = True)
	print()

	print('Weighing and Combining Criteria Method:')
	weigh_combine_criteria(W, CANDIDATES, ['character', 'appearance'], aim_max = True)
	print()


if __name__ == '__main__':
	main()
