"""
PROBLEM: Luxurious Houses
from: codeforces.com
"""

n = int(input())
houses = [int(x) for x in input().split(' ')]
max_sizes = [0] * n
current_max = 0

for i in reversed(range(n)):
	max_sizes[i] = current_max
	if houses[i] > current_max:
		current_max = houses[i]

for i in range(n):
	floors_added = max_sizes[i] - houses[i] + 1
	if floors_added < 0:
		floors_added = 0
	if i < n - 1:
		print(floors_added, end=' ')
	else:
		print(floors_added)
