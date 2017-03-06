"""
PROBLEM: Epic Game
from: codeforces.com
"""

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

simon, antis, heap = [int(x) for x in input().split(' ')]
winner = 1
while True:
	rocks = gcd(simon, heap) if winner == 1 else gcd(antis, heap)
	if rocks <= heap:
		heap -= rocks
		winner = 1 if winner == 0 else 0
	else:
		break
print(winner)

