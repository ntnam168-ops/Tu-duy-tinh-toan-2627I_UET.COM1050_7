def gt(n):
	if not n:
		return 1
	return n * gt(n - 1)
q = int(input())
res = 0
for i in range(q):
	n, k = map(int, input().split())
	res += gt(n) / gt(k) / gt(n - k)
print(int(res))