sits = []

with open("data.txt", "r") as f:
	for line in f:
		sits.append(line.split("\n")[0])

tabPom = [0,0,0,0,0,0,0]
tabSit = [0,0,0]
suma, sumaSit, sitID, highID = 0, 0, 0, 0

for sit in sits:
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
	sitID = suma * 8 + sumaSit
	if (sitID > highID):
		highID = sitID
	suma,sumaSit = 0, 0

print(highID)	


	
