def normalize(w):
	s = sum(w.values())
	for key in w:
		w[key] /= s
	return w


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
		self.__w = W
		for i, key in enumerate(self.__w):
			self.__w[key] = w[i]

	def ws(self):
		return self.__w.values()

	def __str__(self):
		return self.__n
