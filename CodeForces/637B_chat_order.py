"""
PROBLEM: Chat Order
from: codeforces.com
"""

def print_in_order(stack):
    names_appeared = set()
    while stack:
        name = stack.pop()
        if not name in names_appeared:
            print name
            names_appeared.add(name)

n = int(input())
my_stack = []

for _ in range(n):
    my_stack.append(input())

print_in_order(my_stack)
