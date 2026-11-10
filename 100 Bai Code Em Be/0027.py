n = int(input())
def f(x):
	return x * (x + 1) // 2
print(3 * f(n // 3) + 5 * f(n // 5) - 15 * f(n // 15))