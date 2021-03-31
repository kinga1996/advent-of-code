with open('data.txt', 'r') as f:
    rules = f.read()

rules = rules.strip().split('\n')

rules_splitted = []

for item in rules:
    rules_splitted.append(item.replace('.', '').split(' contain '))

rules_dict = {}
for item in rules_splitted:
    temp = {}
    key = item[0].strip().split(' ')
    if 'no other' not in item[1]:
        for i in item[1].split(','):
            stripped = (i.strip().split(' '))
            temp[(stripped[1] + ' ' + stripped[2])] = int(stripped[0])
    rules_dict[key[0] + ' ' + key[1]] = temp

def count_inside(bag, rules):
    return sum(rules[bag][item] * (1 + count_inside(item, rules)) for item in rules[bag])

print(count_inside('shiny gold', rules_dict))