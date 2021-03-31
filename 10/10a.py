adapters = []

with open("data.txt", "r") as f:
	for l in f:
		adapters.append(int(l.split("\n")[0]))

jolt, maxJolt, currentJolt = 0, 0, 0
tabPom, tabPom2 = [], []
i = 1

for adapter in adapters:
	if maxJolt < adapter:
		maxJolt = adapter

while currentJolt <= maxJolt:
	for adapter in adapters:
		if currentJolt == adapter:
			tabPom.append(currentJolt)
	currentJolt = currentJolt + 1

while i < len(tabPom):
	tabPom2.append(tabPom[i] - tabPom [i-1])
	i = i+1

przeskok1 = tabPom2.count(1) + 1
przeskok3 = tabPom2.count(3) + 1

print(przeskok1 * przeskok3)
