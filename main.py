from prettytable import PrettyTable
from input import CANDIDATES
from candidate import W


def make_table(w, c):
	table = PrettyTable()
	table.add_column('Candidate \\ Criteria', [v for v in c.values()])
	for key in w:
		table.add_column(key, [c[k].ws()[key] for k in c])
	print(table)


def main():
	make_table(W, CANDIDATES)


if __name__ == '__main__':
	main()
