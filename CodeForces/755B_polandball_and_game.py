"""
PROBLEM: PolandBall and Game
codeforces.com
"""

def get_n_of_shared_words(x, y):
	x_words = dict()
	for i in range(x):
		x_words[input()] = 1

	shared = 0
	for i in range(y):
		if input() in x_words:
			shared += 1
	return shared

poland, enemy = [int(x) for x in input().split(' ')]
shared = get_n_of_shared_words(poland, enemy)

if poland > enemy:
	print('YES')
else:	
	poland -= shared
	enemy -= shared

	if shared % 2 == 0:
		if poland <= enemy:
			print('NO')
		else:
			print('YES')
	else:
		if enemy <= poland:
			print('YES')
		else:
			print('NO')
