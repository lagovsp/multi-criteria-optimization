from tools import show_table, normalize_matrix, norm_list
from termcolor import colored
import numpy as np


def pairwise_comparison(i, j, mci):
	if (i in mci and j in mci) or (i not in mci and j not in mci):
		return 0.5
	if i in mci and j not in mci:
		return 1
	else:
		return 0


def make_weights_vector(criteria, mci):
	alpha = []
	for i in range(len(criteria)):
		buffer = []
		for j in range(len(criteria)):
			if not i == j:
				buffer.append(pairwise_comparison(i, j, mci))
		alpha.append(sum(buffer))
	return alpha


def matrix_vector_multiply(m, v):
	vec = []
	for line in m:
		buffer = []
		for i, el in enumerate(line):
			buffer.append(el * v[i])
		vec.append(sum(buffer))
	return vec


def weigh_combine_criteria(w, c, main_criteria, aim_max = True):
	c_indexes = [[it[0] for it in w].index(c) for c in main_criteria]
	print(f'Selected criteria {main_criteria}')
	av = norm_list(make_weights_vector([it[0] for it in w], c_indexes))
	fv = matrix_vector_multiply(normalize_matrix(show_table(w, c)), av)
	print(f'Normalized criteria weights vector: {av}')
	print(f'After multiplying: {fv}')
	if aim_max:
		print('We maximize the concerned parameters ' + colored(f'{main_criteria}', 'green'))
		ind = np.array(fv).argmax()
	else:
		print('We minimize the concerned parameters ' + colored(f'{main_criteria}', 'green'))
		ind = np.array(fv).argmin()
	print(f'The most suitable option is ' + colored(f'{c[ind].__str__()}', 'red') + f' {c[ind].ws()}')
