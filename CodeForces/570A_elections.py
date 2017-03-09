"""
PROBLEM: Elections
from: codeforces.com
"""

def get_winner(results, cand_n):
	current_winner = (0, 0)
	for index_cand in range(cand_n):
		if current_winner[1] < results[index_cand]:
			current_winner = (index_cand, results[index_cand])
	return current_winner

cand, cities = [int(x) for x in input().split(' ')]
wins = [0] * cand
for index_city in range(cities):
	res = [int(x) for x in input().split(' ')]
	wins[get_winner(res, cand)[0]] += 1
print(get_winner(wins, cand)[0] + 1)
