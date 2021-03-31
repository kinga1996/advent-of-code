bags = []

with open("data.txt", "r") as f:
	for line in f:
		bags.append(line.split("\n")[0])

suma=0
tabPakiet = []
boolBags = 0

for bag in bags:
	if (bag.count("shiny gold") and bag[0:10]!="shiny gold"):
		tabPakiet.append(bag.split(" bags contain")[0])

while (boolBags == 0):
	tabPom = []
	for pakiet in tabPakiet:
		for bag in bags:
			if (bag.count(pakiet)):
				tabPom.append(bag.split(" bags contain")[0])
	tabPom = list(set(tabPom))
	tabPakiet = list(set(tabPakiet))
	if len(tabPom) != len(tabPakiet):
		boolBags = 0
		tabPakiet = tabPom
	else:
		boolBags = 1

print(len(tabPom), len(tabPakiet))
