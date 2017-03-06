import sys

t = int(input().strip())
for _ in range(t):
	n, m = [int(x) for x in input().strip().split(' ')]
	matrix = [[0 for _ in range(m)] for _ in range(n)]
	x, y = [int(x) for x in input().strip().split(' ')]
	final_x, final_y = [int(x) for x in input().strip().split(' ')]
	is_final = False
	x -= 1
	y -= 1
	final_x -= 1
	final_y -= 1
	matrix[x][y] = 1

	if final_y == 0 or final_y == m - 1:
		if final_x > x:
			print('Back')
		elif final_x < x:
			print('Front')
		else:
			print('Front')
		sys.exit()

	while True:
		if x == final_x and y == final_y:
			is_final = True
		if y < m - 1 and matrix[x][y + 1] == 0:
			if is_final:
				print('Right')
				break
			y += 1
			matrix[x][y] = 1
			if x != final_x:
				y = m - 1
				matrix[x][y] = 1
				matrix[x][y - 1] = 1
		elif y > 0 and matrix[x][y - 1] == 0:
			if is_final:
				print('Left')
				break
			y -= 1
			matrix[x][y] = 1
			if x != final_x:
				y = 0
				matrix[x][y] = 1
				matrix[x][y + 1] = 1
		elif x > 0 and matrix[x - 1][y] == 0:
			if is_final:
				print('Front')
				break
			x -= 1
			matrix[x][y] = 1
		elif x < n - 1 and matrix[x + 1][y] == 0:
			if is_final:
				print('Back')
				break
			x += 1
			matrix[x][y] = 1			
		else:
			print('Over')
			break		