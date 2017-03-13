"""
PROBLEM: Passwords
from: codeforces.com
"""

n, tries = [int(x) for x in input().split(' ')]
lengths = [0] * 100

for _ in range(n):
	lengths[len(input()) - 1] += 1

correct_length = len(input())
current_seconds = 0
current_tries = 0
for i in range(100):
	if lengths[i] > 0:
		if i + 1 == correct_length:			
			print(current_seconds + 1, end=' ')
			current_seconds += lengths[i] + (int((lengths[i] + current_tries - 1) / tries) * 5)
			print(current_seconds)
			break
		else:			
			current_seconds += lengths[i] + (int((lengths[i])/tries) * 5)
			current_tries += lengths[i]%tries
			if current_tries >= tries:
				current_seconds += 5
				current_tries %= tries
			
