lines = []

with open("data.txt", "r") as f:
	for l in f:
		lines.append(l.split("\n")[0])

licznik = 24
suma = 0

while licznik < len(lines):
	tabPom = []
	for i in range(25):
		for j in range(25):
			if i != j: 
				suma = int(lines[licznik - i - 1]) + int(lines[licznik - j - 1])
				if int(suma) != int(lines[licznik]):
					tabPom.append(0)
				else:
					tabPom.append(1)
	if tabPom.count(1):
		print("good")
	else:
		print(licznik, lines[licznik])
		licznik = 100000
	licznik = licznik + 1