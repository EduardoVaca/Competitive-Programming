"""
PROBLEM: The Football Fest
from: hackerearth.com
"""

t = int(input().strip())
for rep in range(t):
    n, current_id = [x for x in input().strip().split(' ')]
    stack = []

    for i in range(int(n)):
        values = [x for x in input().strip().split(' ')]
        pass_type = values[0]
        if pass_type == 'B':
            temp_id = stack.pop()
            stack.append(current_id)
            current_id = temp_id
        else:
            stack.append(current_id)
            current_id = values[1]
    print('Player {}'.format(current_id))
