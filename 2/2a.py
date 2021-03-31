passwords = []

with open("data.txt", "r") as f:
	for line in f:
		passwords.append(line.split("\n")[0].split(" "))

number = []
counter = 0
howMuch = 0

for password in passwords:
	number = password[0].split("-")
	counter = password[2].count(password[1][0])
	if (counter >= int(number[0]) and counter <= int(number [1])):
		howMuch = howMuch + 1

print(howMuch)