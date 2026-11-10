n, m = map(int, input().split())
def f(n):
	return n // 3 + n // 5 - n // 15
def f1(n):
	n -= n & 1
	n >>= 1
	return n * (n + 1)
print(f(m) - f(n - 1), f1(m) - f1(n - 1))