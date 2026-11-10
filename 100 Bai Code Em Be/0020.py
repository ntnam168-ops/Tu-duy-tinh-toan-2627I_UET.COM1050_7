n = int(input())
n //= 1000
a = [5, 2, 1]
for x in a:
	print(n // x, end = " ")
	n %= x