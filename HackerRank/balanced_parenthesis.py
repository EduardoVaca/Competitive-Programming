"""
PROBLEM: Balanced Brackets
from: hackerranck.com
"""

n = int(input().strip())
for _ in range(n):
    stack = []
    brackets = input().strip()
    balanced = True
    for b in brackets:        
        if b == '(' or b == '{' or b == '[':
            stack.append(b)
        elif b == ')' or b == '}' or b == ']':
            if not stack:
                balanced = False
                break
            elif b == ')' and stack.pop() != '(':
                balanced = False
                break
            elif b == ']' and stack.pop() != '[':
                balanced = False
                break
            elif b == '}' and stack.pop() != '{':
                balanced = False
                break
    if not stack and balanced:
        print('YES')
    else:
        print('NO')
