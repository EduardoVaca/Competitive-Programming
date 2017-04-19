"""
PROBLEM: Blown Garland
from: codeforces.com
"""

lights_string = input()
missing = {'R': 0, 'B': 0, 'Y': 0, 'G': 0 }
lights = [c for c in lights_string]

for index in range(len(lights)):
	if lights[index] != '!' and index + 4 < len(lights) and lights[index + 4] == '!':
		missing[lights[index]] += 1
		lights[index + 4] = lights[index]

for index in range(len(lights) - 1, -1, -1):
	if lights[index] != '!' and index - 4 > -1 and lights[index - 4] == '!':
		missing[lights[index]] += 1
		lights[index - 4] = lights[index]

print('{} {} {} {}'.format(missing['R'], missing['B'], missing['Y'], missing['G']))
