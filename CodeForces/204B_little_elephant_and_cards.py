"""
PROBLEM: Little Elephants and Cards
from: codeforces.com
"""

import math

def get_min_changes(cards_n, all_numbers, dict1, dict2):
	min_changes = cards_n + 1
	found = False
	for number in all_numbers:
		if number in dict1 and len(dict1[number]) >= math.ceil(cards_n / 2):
			return 0
		else:
			if number in dict1 and number in dict2:
				if len(dict1[number] | dict2[number]) >= math.ceil(cards_n / 2):
					changes = math.ceil(cards_n / 2) - len(dict1[number])
					if changes < min_changes:
						min_changes = changes
						found = True
			elif number in dict2 and len(dict2[number]) >= math.ceil(cards_n / 2):
				if math.ceil(cards_n / 2) <= min_changes:
					min_changes = math.ceil(cards_n / 2)
					found = True

	if found:
		return min_changes
	else:
		return -1


n = int(input())
upper_dict = dict()
lower_dict = dict()
numbers = set()

for i in range(n):
	card_upper, card_lower = [int(x) for x in input().split(' ')]

	if card_upper in upper_dict:
		upper_dict[card_upper].add(i)
	else:
		upper_dict[card_upper] = {i}

	if card_lower in lower_dict:
		lower_dict[card_lower].add(i)
	else:
		lower_dict[card_lower] = {i}

	numbers.add(card_upper)
	numbers.add(card_lower)

print(get_min_changes(n, numbers, upper_dict, lower_dict))

