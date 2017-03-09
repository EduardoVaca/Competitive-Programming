"""
PROBLEM: Vasya the Hipster
from: codeforces.com
"""

red, blue = [int(x) for x in input().split(' ')]
min_socks = min(red, blue)
max_socks = max(red, blue)
print('{} {}'.format(min_socks, int((max_socks- min_socks) / 2)))
