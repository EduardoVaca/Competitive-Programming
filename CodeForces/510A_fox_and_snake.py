"""
PROBLEM: Fox and Snake
from: codeforces.com
"""

rows, cols = [int(x) for x in input().split(' ')]
start = False
for i in range(rows):
	if (i + 1) % 2 != 0:
		[print('#',end='') for _ in range(cols)]
		print()
	else:
		if start:
			print('#',end='')
			[print('.',end='') for _ in range(1, cols)]
			print()
			start = False
		else:
			[print('.',end='') for _ in range(1, cols)]
			print('#')
			start = True