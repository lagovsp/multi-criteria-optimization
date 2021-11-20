from prettytable import PrettyTable
import copy


def norm_list(v):
	s = sum(it for it in v)
	return [it / s for it in v]


def matrix(cs):
	return [ci.ws() for ci in [c for c in cs]]


def show_matrix(m):
	table = PrettyTable()
	for i in m:
		table.add_row(i)
	print(table)


def show_table(w, cs):
	table = PrettyTable()
	m = matrix(cs)
	table.add_column('Candidate \\ Criteria', [c.__str__() for c in cs])
	for i in range(len(w)):
		table.add_column([it[0] for it in w][i], [line[i] for line in m])
	print(table)
	return m


def normalize_matrix(m, ps = None):
	mat = copy.deepcopy(m)
	for j in range(len(m[0])):
		if not j == ps:
			c_sum = sum([i[j] for i in m])
			for line in mat:
				line[j] /= c_sum
	return mat
