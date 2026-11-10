n, m = map(int, input().split())
def f(n):
	return n * (n + 1) // 2
print(f(m) - f(n - 1))