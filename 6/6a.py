questions = []

with open("data.txt", "r") as f:
	for line in f:
		questions.append(line.split("\n")[0])

alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "q", "s", "t", "u", "v", "w", "x", "y", "z"]
tabPom = []
suma = 0

for a in range(26):
	tabPom.append(1)

for question in questions:
	if (question != ""):
		for a in range(26):
			if (tabPom[a] == 1):
				tabPom[a] = question.count(alf[a])
	else:
		for a in range(26):
			suma = suma + tabPom[a]
		print(suma)
		for a in range(26):
			tabPom[a] = 1