b, a = map(int, input().split())
for i in range(a):
	for j in range(b):
		if not i or i == a - 1 or not j or j == b - 1:
			print('*', end = " ")
		else:
			print(' ', end = " ")
	print()