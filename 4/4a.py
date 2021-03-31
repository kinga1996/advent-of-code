passports = []

with open("data.txt", "r") as f:
	for line in f:
		passports.append(line.split("\n\n")[0].split("\n")[0])

byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0
suma, howMuch= 0, 0

for i in range(958):
	if (passports[i].count("byr") == 1):
		byr = byr + 1
	if (passports[i].count("iyr") == 1):
		iyr = iyr + 1
	if (passports[i].count("eyr") == 1):
		eyr  = eyr  + 1
	if (passports[i].count("hgt") == 1):
		hgt = hgt + 1
	if (passports[i].count("hcl") == 1):
		hcl = hcl + 1
	if (passports[i].count("ecl") == 1):
		ecl  = ecl  + 1
	if (passports[i].count("pid") == 1):
		pid = pid + 1
	if (passports[i].count("cid") == 1):
		cid  = cid  + 1
	if (passports[i] == ""):
		if (byr==1 and iyr==1 and eyr ==1 and hgt==1 and hcl==1 and ecl==1 and pid==1):
			howMuch = howMuch + 1
		byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0

print(howMuch)