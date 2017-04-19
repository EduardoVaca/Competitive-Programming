"""
PROBLEM: Counting-out Rhyme
from: codeforces.com
"""
kids_n, rounds_n = [int(x) for x in input().split(' ')]
rounds = [int(x) for x in input().split(' ')]

kids = [x+1 for x in range(kids_n)]

leader = 0

for i in range(rounds_n):
	eliminated_index = (leader + rounds[i]) % kids_n
	if eliminated_index == kids_n - 1:
		leader = 0
	else:
		leader = eliminated_index	
	eliminated_kid = kids.pop(eliminated_index)
	kids_n -= 1

	if i == rounds_n - 1:
		print(eliminated_kid)
	else:
		print(eliminated_kid, end=' ')
