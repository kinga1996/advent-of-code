lines = []

with open("data.txt", "r") as f:
	for l in f:
		lines.append(l.split("\n")[0].split(" "))

licznik=0
tabPom = []
accX = 0

while licznik <= len(lines):
	if (lines[licznik][0] == "acc"):
		accX = accX + int(lines[licznik][1])
		licznik = licznik + 1
	elif (lines[licznik][0] == "jmp"):
		licznik = licznik + int(lines[licznik][1])
	else:
		licznik = licznik + 1
	for i in tabPom:
		if licznik == int(i):	
			licznik = 1000
			tabPom = []
	tabPom.append(licznik)

print(accX)