bombs = [[False for y in range(8)] for x in range(5)]
bombs[0][1] = True
bombs[3][5] = True
bombs[4][7] = True
for row in bombs:
	for column in row:
		if not column:
			print('#', end='')
		else:
			print('*', end='')
	print()