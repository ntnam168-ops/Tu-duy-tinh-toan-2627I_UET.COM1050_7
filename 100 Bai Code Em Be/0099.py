def cp(n) -> bool:
	if n < 0:
		return False
	d = int(n ** 0.5)
	return d * d == n
ar = list(map(int, input().split()))
res, cnt = 0, 0
for x in ar:
	if cp(x):
		res += x
		cnt += 1
print(f"{res / cnt :.1f}" if cnt else "-")