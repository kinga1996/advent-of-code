import copy


sits = []

with open("data.txt", "r") as f:
	for l in f:
		sits.append(l.split("\n")[0])


sits = [list(x) for x in sits]


def check_neighbours(sits, row, col, max_row, max_col):
	l = []

	if col - 1 >= 0:
		l.append(sits[row][col-1])
		if row -1 >= 0:
			l.append(sits[row-1][col-1])
		if row + 1 < max_row:
			l.append(sits[row+1][col-1])

	if col + 1 < max_col:
		l.append(sits[row][col+1])

		if row - 1 >= 0:
			l.append(sits[row-1][col+1])
		if row + 1 < max_row:
			l.append(sits[row+1][col+1])

	if row - 1 >= 0:
		l.append(sits[row-1][col])

	if row + 1 < max_row:
		l.append(sits[row+1][col])

	return l


def apply_rules(sits, i, j, l, m_sits):
	if l.count('#') == 0 and sits[i][j] == 'L':
		m_sits[i][j] = '#'
	elif l.count('#') >= 4 and sits[i][j] == '#':
		m_sits[i][j] = 'L'

	return m_sits


max_r = len(sits)
max_c = len(sits[0])

mod_sits = copy.deepcopy(sits)
counter = 0

while sits != mod_sits or counter == 0:
	sits = copy.deepcopy(mod_sits)
	mod_sits = copy.deepcopy(sits)

	for r in range(len(sits)):
		for c in range(len(sits[0])):
			neigh = check_neighbours(sits, r, c, max_r, max_c)
			mod_sits = apply_rules(sits, r, c, neigh, mod_sits)

	counter += 1

counter -= 1
results = [x.count('#') for x in mod_sits]
print(sum(results))
