passwords = []

with open("data.txt", "r") as f:
	for line in f:
		passwords.append(line.split("\n")[0].split(" "))

number = []
yes = 0

for password in passwords:
	number = password[0].split("-")
	if (password[2][int(number[0])-1] == password[1][0] and password[2][int(number[1])-1] != password[1][0]):
		print("yes", password[2], int(number[0]), int(number[1]), password[1][0])
		yes = yes + 1
	elif (password[2][int(number[0])-1] != password[1][0] and password[2][int(number[1])-1] == password[1][0]):
		print("yes", password[2], int(number[0]), int(number[1]), password[1][0])
		yes = yes + 1

print(yes)



