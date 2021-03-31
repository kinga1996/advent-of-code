a = []

with open("data.txt", "r") as f:
	for line in f:
		a.append(line.split("\n")[0])

for i in range(200):
	for j in range(200):
		if (i != j):
			suma = int(a[i]) + int(a[j])
			if (suma == 2020):
				print (a[i], a[j], 'iloczyn: ', int(a[i])*int(a[j]))