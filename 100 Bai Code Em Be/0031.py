n, m = map(int, input().split())
def f(n):
	return n // 3
print(f(m) - f(n - 1))