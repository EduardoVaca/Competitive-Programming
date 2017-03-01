"""
PROBLEM: Micro and Array Update
from: hackerearth.com
"""

t = int(input().strip())
for _ in range(t):
	n, k = [int(x) for x in input().strip().split(' ')]
	lst = [int(x) for x in input().strip().split(' ')]
	smallest = lst[0]
	for e in lst:
		if e < smallest:
			smallest = e
	if smallest < k:
		print(k - smallest)
	else:
		print('0')
