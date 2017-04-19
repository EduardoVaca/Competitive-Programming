"""
PROBLEM: Rebranding
From: codeforces.com
"""

letters, designers = [int(x) for x in input().split(' ')]
name = input()
alphabet_dict = {x: x for x in range(26)}
alphabet_arr = [(x + 97) for x in range(26)]

def print_dict(dict_al):
	for key, value in dict_al.items():
		print('{}: {}'.format(chr(key), chr(value)))

for _ in range(designers):
	letter1, letter2 = input().split(' ')
	who_has_1 = alphabet_dict[ord(letter1) - 97]
	who_has_2 = alphabet_dict[ord(letter2) - 97]
	alphabet_arr[who_has_1] = ord(letter2)
	alphabet_arr[who_has_2] = ord(letter1)
	alphabet_dict[ord(letter1) - 97] = who_has_2
	alphabet_dict[ord(letter2) - 97] = who_has_1
	

for letter in name:
	print(chr(alphabet_arr[ord(letter) - 97]), end='')
print()