"""
PROBLEM: Snacktower
from: codeforces.com
"""

def find_smaller_continiously(size, lst):
	print(size, end='')
	while size > 1:
		size -= 1
		if lst[size - 1] == 1:
			print(' {}'.format(size), end='')
		else:
			break
	print()
	return size

max_size = int(input())
snacks = [int(x) for x in input().split(' ')]
already_fallen = [0] * max_size

for snack in snacks:
	if snack == max_size:
		max_size = find_smaller_continiusly(max_size, already_fallen)
	else:
		already_fallen[snack - 1] = 1
		print()