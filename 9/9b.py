lines = []

with open("data.txt", "r") as f:
	for l in f:
		lines.append(l.split("\n")[0])

licznik = 0
what = 0

while licznik < len(lines):
	a = 1
	suma = 0
	while suma < 466456641:
		suma = suma + int(lines[licznik - a])
		if suma == 466456641:
			print(licznik, a)
			k = 1
			min = int(lines[licznik - a])
			max = int(lines[licznik - a])
			while k <= a:
				if int(lines[licznik - k]) > max:
					max = int(lines[licznik - k])
				if int(lines[licznik - k]) < min:
					min = int(lines[licznik - k])
				k = k + 1
			what = min + max
			print(what)
		a=a+1
	licznik = licznik + 1
