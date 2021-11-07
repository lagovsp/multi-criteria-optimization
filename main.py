from prettytable import PrettyTable
from candidate import *
from input import *


def make_table(W, C):
	titles = ['Candidate \\ Criteria']
	table = PrettyTable()
	table.add_column(titles[0], [c.__str__() for c in C.values()])
	for i, key in enumerate(W.keys()):
		print(key)
		print([c.ws()[i] for c in C])
		# table.add_column(key, [c.ws()[i] for c in C.values()])
	print(table)


def main():
	make_table(W, CANDIDATES)


if __name__ == '__main__':
	main()
