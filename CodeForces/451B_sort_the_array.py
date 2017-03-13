"""
PROBLEM: Sort the array
from: codeforces.com
"""

n = int(input())
array = [int(x) for x in input().split(' ')]
min_edge = 0
max_edge = 10000000000
start = end = -1
in_rotation = False
already_rotated = False
not_found = False

for i in range(n):
	if already_rotated:
		if i + 1 < n and array[i] > array[i + 1]:
			not_found = True
			break
	else:		
		if i + 1 < n and not in_rotation and array[i] > array[i + 1]:
			start = i
			min_edge = 0 if i - 1 < 0 else array[i - 1]
			in_rotation = True
		if i + 1 < n and in_rotation and array[i] < array[i + 1]:
			end = i			
			max_edge = array[i + 1]
			if array[start] > max_edge or array[end] < min_edge:
				not_found = True
				break
			already_rotated = True

if not_found:
	print('no')
elif start == end and start == -1:
	print('yes\n1 1')
else:
	if not already_rotated:		
		end = n - 1
	if array[start] > max_edge or array[end] < min_edge:
		print('no')
	else:
		print('yes\n{} {}'.format(start + 1, end + 1))