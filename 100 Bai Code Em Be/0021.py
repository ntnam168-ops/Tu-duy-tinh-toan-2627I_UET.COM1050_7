n = int(input())
if n == 1:
	print(12000)
elif n <= 30:
	print((n - 1) * 10000 + 12000)
else:
	print(29 * 10000 + 12000 + (n - 30) * 9000)