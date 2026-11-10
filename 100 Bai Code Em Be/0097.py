def nt(n):
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if not n % i:
			return False
	return True
ar = list(map(int, input().split()))
res = 0
for i in ar:
	if nt(i):
		res += 1
print(res)