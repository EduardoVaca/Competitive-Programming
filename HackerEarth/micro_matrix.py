"""
PROBLEM:  Micro and Matrix
from: hackerearth.com
"""

class Square:

	def __init__(self, f_i, f_j, l_i, l_j):
		self.first_i = f_i
		self.first_j = f_j
		self.last_i = l_i
		self.last_j = l_j

	def is_inside(self, x, y):
		return x >= self.first_i and x <= self.last_i and y >= self.first_j and y <= self.last_j


def is_in_previous_squares(lst, i, j):
	for square in lst:
		if square.is_inside(i, j):
			return True
	return False

def find_largest_square(matrix, m):
	lst_squares = []
	size = 0
	max_size = 0
	current = 0
	for i in range(m):
		for j in range(m):
			current = matrix[i][j]
			if is_in_previous_squares(lst_squares, i, j):
				break
			size = 0
			for j_2 in range(j, m):
				if matrix[i][j_2] == current:
					size += 1
				else:
					break			
			square = True
			i_min = min(m - i,  i + size)
			j_min = min(m - j, j + size)
			size = min(i_min, j_min)
			for j_2 in range(j, j + size):
				for i_2 in range(i, i + size):
					if matrix[i_2][j_2] != current:
						square = False
						break
			if square and size > 2:
				lst_squares.append(Square(i, j, i + size - 1, j + size - 1))
			if square and size > max_size:
				max_size = size			
			j += size
	return max_size



t = int(input().strip())
for _ in range(t):
	m = int(input().strip())
	matrix = [[int(x) for x in input().strip().split(' ')] for y in range(m)]
	print(find_largest_square(matrix, m))
