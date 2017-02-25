"""
PROBLEM: Signal Range
from: hackerearth.com
"""

t = int(input().strip())

for __ in range(t):
    n = int(input().strip())
    lst = [int(x) for x in input().strip().split(' ')]
    signal_lst = []
    for i in range(n):
        if i == 0:
            signal_lst.append(1)
        elif lst[i - 1] > lst[i]:
            signal_lst.append(1)
        else:
            current_index = (i - 1) - signal_lst[i - 1]
            while current_index >= 0 and lst[i] >= lst[current_index]:
                current_index = current_index - signal_lst[current_index]
            signal_lst.append(i - current_index)
    for i in range(n):
        if i < n - 1:
            print(signal_lst[i], end = ' ')
        else:
            print(signal_lst[i])
