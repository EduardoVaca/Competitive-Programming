"""
PROBLEM: Vanya and Fence
from: codeforces.com
"""

n, fence = [int(x) for x in input().split(' ')]
kids = [int(x) for x in input().split(' ')]

sum = 0
for k in kids:
	sum += 1 if k <= fence else 2
print(sum)