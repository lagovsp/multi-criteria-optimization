from matplotlib import pyplot as plt


def pareto(w, c, main_criteria, aim_max = True):
	crind = [[it[0] for it in w].index(c) for c in main_criteria]
	plt.title(f'Pareto Set Method')
	print(f'Selected crtiteria {main_criteria}')
	plt.xlabel(w[crind[0]][0])
	plt.ylabel(w[crind[1]][0])
	can_values = []
	for i, can in enumerate(c):
		can_values.append([can.ws[crind[0]], can.ws[crind[1]]])
		plt.scatter(can.ws[crind[0]], can.ws[crind[1]], label = can.n)
	utopia = []
	if aim_max:
		utopia = [max(can.ws[crind[0]] for can in c), max(can.ws[crind[1]] for can in c)]
	else:
		utopia = [min(can.ws[crind[0]] for can in c), min(can.ws[crind[1]] for can in c)]
	plt.scatter(utopia[0], utopia[1], label = 'utopia')
	distances = [((cv[0] - utopia[0]) ** 2 + (cv[1] - utopia[1]) ** 2) ** 0.5 for cv in can_values]
	plt.legend()
	plt.show()
	best = c[distances.index(min(distances))]
	print(f'The most suitable option is {best.n} {best.ws}')
	return 0
