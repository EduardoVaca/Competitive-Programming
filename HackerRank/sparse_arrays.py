import sys

n = int(input().strip())
words_found = {}
current_word = ''

"""Create dictionary {'word found': times}"""
for i in range(n):
    current_word = input().strip()
    if current_word in words_found:
        words_found[current_word] += 1
    else:
        words_found[current_word] = 1

q = int(input().strip())
queries = []
for i in range(q):
    queries.append(input().strip())

"""Make queries"""
for query in queries:
    if query in words_found:
        print(words_found[query])
    else:
        print('0')
