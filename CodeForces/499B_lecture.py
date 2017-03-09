"""
PROBLEM: Lecture
from: codeforces.com
"""

_, words = [int(x) for x in input().split(' ')]
words_dict = dict()
numbers_dict = dict()
#Store words
for index in range(words):
	w1, w2 = [x for x in input().split(' ')]
	words_dict[w1] = words_dict[w2] = index
	numbers_dict[index] = w1 if len(w1) <= len(w2) else w2  

lecture = [word for word in input().split(' ')]
for word in lecture:
	print(numbers_dict[words_dict[word]], end=' ')
print()