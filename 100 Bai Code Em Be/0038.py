def f(n):
	if n < 2:
		return False
	d = int(n ** 0.5)
	for i in range(2, d + 1):
		if not n % i:
			return False
	return True
n = int(input())
pos = 1
for i in range(n):
	while not f(pos):
		pos += 1
	print(pos, end = " ")
	pos += 1