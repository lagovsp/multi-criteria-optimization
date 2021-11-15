from tools import show_table
from candidate import Candidate


def check_candidate(line, restrictions, lower_border = True):
	for i, it in enumerate(restrictions):
		if Candidate.main_criteria_ind != i:
			if lower_border:
				if line[i] < it:
					return False
			if not lower_border:
				if line[i] > it:
					return False
	return True


def criteria_constraint(w, c, main_criteria, aim_max = True):
	Candidate.main_criteria_ind = [t[0] for t in w].index(main_criteria)
	m = show_table(w, c)
	min_allowed = [0.5 * max(line[i] for line in m) for i in range(len(w))]
	min_allowed[Candidate.main_criteria_ind] = None
	print(f'The lowest values border: {min_allowed}')
	pass_cs = [c[i] for i, line in enumerate(m) if check_candidate(line, min_allowed, lower_border = aim_max)]
	pass_cs.sort(key = Candidate.main_criteria_sort_key, reverse = aim_max)
	print(f'Candidates to meet minimum requirements: {[p.n for p in pass_cs]}')
	print(f'The most suitable option is {pass_cs[0]} {pass_cs[0].ws}')
	return pass_cs[0]
