"""
PROBLEM: Find The Bone
From: codeforces.com
"""

_, _, n = [int(x) for x in input().split(' ')]
holes = {int(x) for x in input().split(' ')}

if 1 in holes:
	print(1)
else:
	current_cup = 1
	for _ in range(n):
		c1, c2 = [int(x) for x in input().split(' ')]
		if c1 == current_cup or c2 == current_cup:
			if c1 == current_cup:
				current_cup = c2
			else:
				current_cup = c1
			if current_cup in holes:				
				break
	print(current_cup)
