ar = list(map(int, input().split()))

def nt(n):
	if n < 2:
		return False
	d = int(n ** 0.5)
	for i in range(2, d + 1):
		if not n % i:
			return False
	return True
res = 0
for i in ar:
	if nt(i):
		res = max(res, i)
if not res:
	print('-')
else:
	print(res)