"""
PROBLEM: Boy or Girl
from: codeforces.com
"""

username = input().strip()
unique_chars = set()
for c in username:
	unique_chars.add(c)
if len(unique_chars) % 2 == 0:
	print('CHAT WITH HER!')
else:
	print('IGNORE HIM!')