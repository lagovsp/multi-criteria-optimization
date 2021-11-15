class Candidate:
	main_criteria_ind = None

	@staticmethod
	def main_criteria_sort_key(c):
		return c.ws[Candidate.main_criteria_ind]

	def __init__(self, n, ws):
		self.n = n
		self.ws = ws

	def __str__(self):
		return self.n


def norm_list(w):
	s = sum(it[1] for it in w)
	return [[it[0], it[1] / s] for it in w]
