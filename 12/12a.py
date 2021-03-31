import math

instructions = []

with open("data.txt", "r") as f:
	for l in f:
		instructions.append(l.split("\n")[0])

west = {90: "north", 180: "east", 270: "south", -90: "south", -180: "east", -270: "north"}
north = {90: "east", 180: "south", 270: "west", -90: "west", -180: "south", -270: "east"}
east = {90: "south", 180: "west", 270: "north", -90: "north", -180: "west", -270: "south"}
south = {90: "west", 180: "north", 270: "east", -90: "east", -180: "north", -270: "west"}

instr = []
tabPom = []
actual = "east"

for i in instructions:
	tabPom.append(i[0])
	tabPom.append(i[1:])
	instr.append(tabPom)
	tabPom = []

e=0
n=0
s=0
w=0

for ins in instr:
	if ins[0] == "E":
		e = e + int(ins[1])
	if ins[0] == "N":
		n = n + int(ins[1])	
	if ins[0] == "S":
		s = s + int(ins[1])	
	if ins[0] == "W":
		w = w + int(ins[1])	
	if ins[0] == "R":
		if actual == "east":
			actual = east[int(ins[1])]
		elif actual == "north":
			actual = north[int(ins[1])]
		elif actual == "west":
			actual = west[int(ins[1])]
		elif actual == "south":
			actual = south[int(ins[1])]
	if ins[0] == "L":
		if actual == "east":
			actual = east[-int(ins[1])]
		elif actual == "north":
			actual = north[-int(ins[1])]
		elif actual == "west":
			actual = west[-int(ins[1])]
		elif actual == "south":
			actual = south[-int(ins[1])]
	if ins[0] == "F":
		if actual == "east":
			e = e + int(ins[1])
		elif actual == "north":
			n = n + int(ins[1])	
		elif actual == "west":
			w = w + int(ins[1])
		elif actual == "south":
			s = s + int(ins[1])	
	print(ins, e, n, s, w, actual)

pl = 0
gd = 0

gd = math.fabs(n - s)
pl = math.fabs(w - e)

print(e, n, s, w, actual )

print(gd + pl )
