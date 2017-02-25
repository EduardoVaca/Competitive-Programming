"""
PROBLEM: Little Monk and Balanced Parentheses
From: hackerearth.com
"""

n = int(input().strip())
lst = [int(x) for x in input().strip().split(' ')]
stack = []
max_balanced = 0
current_balance = 0

for element in lst:
    if element > 0:
        if current_balance > 0 and len(stack):
            current_balance = 0
        stack.append(element)
    elif len(stack):
        peek_element = stack.pop()
        if peek_element == -(element):
            current_balance += 1
        else:
            current_balance = 0
            stack = []
        if current_balance > max_balanced:
            max_balanced = current_balance
print(max_balanced * 2)
