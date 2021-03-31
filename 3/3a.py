ways = []

with open("data.txt", "r") as f:
	for line in f:
		ways.append(line.split("\n")[0])

right= 0
tree = 0
down = 0

for way in ways:
	down = down + 1
	if (down%2 == 1):
		right=right+1
		rightSet = (right%31)-1
		if (way[rightSet] == "#"):
			tree = tree + 1
			print(way, rightSet, way[rightSet], tree)
		else:
			print(way, rightSet, way[rightSet])
	else:
		print(way)

#ma 323 elementy, 31 w bok
print(93*164*82*91*44)