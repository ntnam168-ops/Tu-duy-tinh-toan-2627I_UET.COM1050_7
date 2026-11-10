def cp(n):
	d = int(n ** 0.5)
	return d * d == n
n = int(input())
pos = 0
for i in range(n):
	while not cp(pos):
		pos += 1
	print(pos, end = " ")
	pos += 1