def p(a, b):
	if not b:
		return 1
	return p(a, b - 1) * a
k, x = map(int, input().split())
res = 0
for i in range(k):
	a, n = map(int, input().split())
	res += a * p(x, n)
print(res)