n = int(input())
res = 0
d = int(n ** 0.5)
for i in range(1, d + 1):
	if not n % i:
		res += 2
print(res - (d * d == n))