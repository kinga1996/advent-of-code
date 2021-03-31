import re

passports = []

with open("data.txt", "r") as f:
	for line in f:
		passports.append(line.split("\n\n")[0].split("\n")[0])

byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0
howMuch = 0
birth, line, splitPom = [], [], []
eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def special_match(strg, search=re.compile(r'[0-9a-f]').search):
    return bool(search(strg))

for i in range(958):
	lines = passports[i].split(" ")
	for line in lines:
		if (line.count("byr") == 1):
			splitPom = line.split(":")
			if (int(splitPom[1]) >= 1920 and int(splitPom[1]) <= 2002):
				byr = 1
		if (line.count("iyr") == 1):
			splitPom = line.split(":")
			if (int(splitPom[1]) >= 2010 and int(splitPom[1]) <= 2020):
				iyr = 1
		if (line.count("eyr") == 1):
			splitPom = line.split(":")
			if (int(splitPom[1]) >= 2020 and int(splitPom[1]) <= 2030):
				eyr = 1
		if (line.count("hgt") == 1):
			splitPom = line.split(":")
			if splitPom[1].count("cm"):
				if splitPom[1][0:3].isdigit():
					if (int(splitPom[1][0:3]) >= 150 and int(splitPom[1][0:3]) <= 193):
						hgt = 1
			if splitPom[1].count("in"):
				if (int(splitPom[1][0:2]) >= 59 and int(splitPom[1][0:2]) <= 76):
					hgt = 1
		if (line.count("hcl") == 1):
			splitPom = line.split(":")
			if (splitPom[1][0] == "#" and special_match(splitPom[1][1:7])):
				hcl = 1				
		if (line.count("ecl") == 1):
			splitPom = line.split(":")
			for a in eyeColor:
				if (splitPom[1]==a):
					ecl = 1
		if (line.count("pid") == 1):
			splitPom = line.split(":")
			if len(splitPom[1]) == 9:
				if splitPom[1][1:9].isdigit():
					pid = 1
		if (line == ""):
			if (byr==1 and iyr==1 and eyr ==1 and hgt==1 and hcl == 1 and ecl==1 and pid==1):
				howMuch = howMuch + 1
			byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0

print(howMuch)
	