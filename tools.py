from prettytable import PrettyTable


def matrix(cs):
	return [ci.ws() for ci in [c for c in cs.values()]]


def show_matrix(m):
	table = PrettyTable()
	for i in m:
		table.add_row(i)
	print(table)


def normalize_matrix(m, ps = None):
	print(len(m[0]))
	print(m[0])
	print()
	for j in range(len(m[0])):
		if not j == ps:
			cur_col = [i[j] for i in m]
			print(cur_col)
			c_min = min(cur_col)
			c_max = max(cur_col)
			# print(f'cmin = {c_min}')
			# print(f'cmax = {c_max}')
			for i in range(len(m)):
				m[i][j] = (m[i][j] - c_min) / (c_max - c_min)
		# print(f'after all {[i[j] for i in m]}')
		# print(m)
		# print()

	return m


def show_table(w, c):
	table = PrettyTable()
	m = matrix(c)
	table.add_column('Candidate \\ Criteria', [v for v in c.values()])
	for i, key in enumerate(w):
		table.add_column(key, [line[i] for line in m])
	print(table)
	return m
