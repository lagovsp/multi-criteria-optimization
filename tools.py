from prettytable import PrettyTable


def matrix(cs):
	return [ci.ws for ci in [c for c in cs]]


def show_matrix(m):
	table = PrettyTable()
	for i in m:
		table.add_row(i)
	print(table)


def normalize_matrix(m, ps = None):
	for j in range(len(m[0])):
		if not j == ps:
			cur_col = [i[j] for i in m]
			print(cur_col)
			c_min = min(cur_col)
			c_max = max(cur_col)
			for i in range(len(m)):
				m[i][j] = (m[i][j] - c_min) / (c_max - c_min)
	return m


def show_table(w, cs):
	table = PrettyTable()
	m = matrix(cs)
	table.add_column('Candidate \\ Criteria', [c.n for c in cs])
	for i in range(len(w)):
		table.add_column([it[0] for it in w][i], [line[i] for line in m])
	print(table)
	return m
