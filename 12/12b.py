import math

instructions = []

with open("data.txt", "r") as f:
	for l in f:
		instructions.append(l.split("\n")[0])

instr = []
tabPom = []
actual = "east"

for i in instructions:
	tabPom.append(i[0])
	tabPom.append(i[1:])
	instr.append(tabPom)
	tabPom = []

west = {90: "north", 180: "east", 270: "south", -90: "south", -180: "east", -270: "north"}
north = {90: "east", 180: "south", 270: "west", -90: "west", -180: "south", -270: "east"}
east = {90: "south", 180: "west", 270: "north", -90: "north", -180: "west", -270: "south"}
south = {90: "west", 180: "north", 270: "east", -90: "east", -180: "north", -270: "west"}


estatek=0
nstatek=0
ewaypoint=10
nwaypoint=1
etemp = 0
ntemp = 0

actual1 = "north"
actual2 = "east"

for ins in instr:
	if ins[0] == "E":
		ewaypoint = ewaypoint + int(ins[1])
	if ins[0] == "N":
		nwaypoint = nwaypoint + int(ins[1])	
	if ins[0] == "S":
		nwaypoint = nwaypoint - int(ins[1])	
	if ins[0] == "W":
		ewaypoint = ewaypoint - int(ins[1])	
	if ins[0] == "R":
		if actual2 =="north" and actual1=="east":
			actual2 = north[int(ins[1])]
			actual1 = east[int(ins[1])]
			if actual2 == "west" and actual1 == "north":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "south" and actual1 == "west":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "east" and actual1 == "south":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="east" and actual1=="south":
			actual2 = east[int(ins[1])]
			actual1 = south[int(ins[1])]
			if actual2 == "north" and actual1 == "east":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "west" and actual1 == "north":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "south" and actual1 == "west":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="south" and actual1=="west":
			actual2 = south[int(ins[1])]
			actual1 = west[int(ins[1])]
			if actual2 == "east" and actual1 == "south":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "north" and actual1 == "east":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "west" and actual1 == "north":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="west" and actual1=="north":
			actual2 = west[int(ins[1])]
			actual1 = north[int(ins[1])]
			if actual2 == "north" and actual1 == "east":
				etemp = nwaypoint
				ntemp = -ewaypoint
			elif actual2 == "east" and actual1 == "south":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "south" and actual1 == "west":
				etemp = -nwaypoint
				ntemp = ewaypoint
		nwaypoint = ntemp
		ewaypoint = etemp
	if ins[0] == "L":
		if actual2 =="north" and actual1=="east":
			actual2 = north[-int(ins[1])]
			actual1 = east[-int(ins[1])]
			if actual2 == "west" and actual1 == "north":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "south" and actual1 == "west":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual1 == "east" and actual1 == "south":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="east" and actual1=="south":
			actual2 = east[-int(ins[1])]
			actual1 = south[-int(ins[1])]
			if actual2 == "north" and actual1 == "east":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "west" and actual1 == "north":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual1 == "south" and actual1 == "west":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="south" and actual1=="west":
			actual2 = south[-int(ins[1])]
			actual1 = west[-int(ins[1])]
			if actual2 == "east" and actual1 == "south":
				etemp = -nwaypoint
				ntemp = ewaypoint
			elif actual2 == "north" and actual1 == "east":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "west" and actual1 == "north":
				etemp = nwaypoint
				ntemp = -ewaypoint
		elif actual2 =="west" and actual1=="north":
			actual2 = west[-int(ins[1])]
			actual1 = north[-int(ins[1])]
			if actual2 == "north" and actual1 == "east":
				etemp = nwaypoint
				ntemp = -ewaypoint
			elif actual2 == "east" and actual1 == "south":
				etemp = -ewaypoint
				ntemp = -nwaypoint
			elif actual2 == "south" and actual1 == "west":
				etemp = -nwaypoint
				ntemp = ewaypoint
		
		nwaypoint = ntemp
		ewaypoint = etemp

	if ins[0] == "F":
		estatek = estatek + ewaypoint * int(ins[1])
		nstatek = nstatek + nwaypoint * int(ins[1])

	if (ewaypoint < 0 and actual1 == "east"):
		actual2 = "west"
		actual1 = "north"

	if (ewaypoint < 0 and actual2 == "east"):
		actual1 = "west"
		actual2 = "south"

	if (ewaypoint > 0 and actual1 == "west"):
		actual2 = "east"
		actual1 = "south"

	if (ewaypoint > 0 and actual2 == "west"):
		actual1 = "east"
		actual2 = "north"


	if (nwaypoint < 0 and actual1 == "north"):
		actual1 = "west"
		actual2 = "south"

	if (nwaypoint < 0 and actual2 == "north"):
		actual2 = "east"
		actual1 = "south"

	if (nwaypoint > 0 and actual1 == "south"):
		actual1 = "east"
		actual2 = "north"

	if (nwaypoint > 0 and actual2 == "south"):
		actual2 = "west"
		actual1 = "north"

	if (nwaypoint < 0 and ewaypoint < 0):
		actual1 = "west"
		actual2 = "south"

	if (nwaypoint > 0 and ewaypoint > 0):
		actual1 = "east"
		actual2 = "north"


print(math.fabs(estatek)+ math.fabs(nstatek))
