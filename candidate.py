def normalize(w):
	s = sum(w.values())
	return {k: w[k] / s for k in w}


# order matters
W = normalize({
	'education': 8,
	'physical-condition': 2,
	'appearance': 6,
	'character': 7
})


class Candidate:
	def __init__(self, n, w):
		self.__n = n
		self.__w = {k: w[i] for i, k in enumerate(W)}

	def ws(self):
		return self.__w

	def __str__(self):
		return self.__n
