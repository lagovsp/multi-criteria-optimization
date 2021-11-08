from tools import *
from enum import Enum


def crit_const(w, c, mc):
	m = show_table(w, c)
	min_allowed = [0.5 * max(col) for col in m]
	print(min_allowed)
	no_touch = None
	for i, k in enumerate([n for n in w.keys()]):
		if k == mc:
			no_touch = i
	m = normalize_matrix(m, ps = no_touch)
	show_matrix(m)
