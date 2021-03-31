sits = []

with open("data.txt", "r") as f:
	for line in f:
		sits.append(line.split("\n")[0])

tabPom = [0,0,0,0,0,0,0]
tabSit = [0,0,0]
tabTaken, tabID = [], []

for sit in sits:
	suma, sumaSit = 0, 0
	for i in range(7):
		if (sit[i] =="F"):
			tabPom[i] = 0
		else:
			tabPom[i] = 1
	for i in range(7):
		suma = suma + tabPom[i] * (2**(6-i))
	for i in range(3):
		if (sit[7+i] =="L"):
			tabSit[i] = 0
		else:
			tabSit[i] = 1
	for i in range(3):
		sumaSit = sumaSit + tabSit[i] * (2**(2-i))
	sitID = suma*8 + sumaSit
	tabTaken.append([suma, sumaSit])
	tabID.append(sitID)

for x in range(128):
	for y in range(8):
		if (tabTaken.count([x, y]) == 0):
			sitID = x*8 + y
			if (tabID.count((x*8 + y)-1) == 1 and tabID.count((x*8 + y)+1) == 1):
				print(x, y, sitID)

