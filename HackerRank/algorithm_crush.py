"""
PROBLEM: Algorithmic Crush
from: https://www.hackerrank.com/challenges/crush
"""

import sys

n, m = [int(x) for x in input().strip().split(' ')]
lst = [0] * n

for i in range(m):
    start, end, value = [int(x) for x in input().strip().split(' ')]
    lst[start - 1] += value
    if end < n:
        lst[end] += -value

max_value = 0
for i in range(n):
    if i > 0:
        lst[i] += lst[i - 1]
    if lst[i] > max_value:
        max_value = lst[i]

print(max_value)
