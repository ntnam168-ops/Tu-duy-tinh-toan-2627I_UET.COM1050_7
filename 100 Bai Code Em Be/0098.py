ar = list(map(int, input().split()))

def nt(n):
	if n < 2:
		return False
	d = int(n ** 0.5)
	for i in range(2, d + 1):
		if not n % i:
			return False
	return True
res, cnt = 0, 0
for i in ar:
	if nt(i):
		res += i
		cnt += 1
if not cnt:
	print('-')
else:
	print(f"{res / cnt:.2f}")