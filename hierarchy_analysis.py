from prettytable import PrettyTable
from tools import show_table
from sty import *


def make_pairwise_comparison_matrix(vec, cr_name):
	m = [[el1[1] / el2[1] for el2 in vec] for el1 in vec]
	table = PrettyTable()
	table.add_column('', [el[0] for el in vec])
	for i, can in enumerate(vec):
		table.add_column(can[0], [line[i] for line in m])
	bg.orange = Style(RgbBg(255, 150, 50))
	print(bg.orange + fg.black + f'Table for {cr_name}' + fg.rs + bg.rs)

	print(table)
	return m


def find_consistency_rel(m):
	return 0


def hierarchy_analysis(w, c, aim_max = True):
	print(fg.green + 'Main table' + fg.rs)
	mat = show_table(w, c)
	for ind in range(len(w)):
		m = make_pairwise_comparison_matrix([[c[i].__str__(), l[ind]] for i, l in enumerate(mat)], w[ind][0])
	return 0
