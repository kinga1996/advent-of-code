a = []

with open("data.txt", "r") as f:
	for line in f:
		a.append(line.split("\n")[0])

for i in range(200):
	for j in range(200):
		for k in range(200):
			if (i != j):
				if (j != k):
					suma = int(a[i]) + int(a[j]) + int(a[k])
					if (suma == 2020):
						print (a[i], a[j], a[k], 'iloczyn: ', int(a[i])*int(a[j])*int(a[k]))