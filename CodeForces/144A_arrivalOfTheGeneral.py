"""
PROBLEM: A. Arrival of the General
from: codeforces.com
"""

def find_i_smallest_i_biggest(lst, size):
    smallest = 101
    biggest = 0
    i_smallest = i_biggest = 0
    for i in range(size):
        if lst[i] > biggest:
            biggest = lst[i]
            i_biggest = i
        if lst[i] <= smallest:
            smallest = lst[i]
            i_smallest = i
    return (i_smallest, i_biggest)

size = int(input().strip())
lst = [int(x) for x in input().strip().split(' ')]
i_smallest, i_biggest = find_i_smallest_i_biggest(lst, size)
mov = abs(size - 1 - i_smallest)
mov += i_biggest

if i_smallest < i_biggest:    
    mov -= 1

print(mov)
