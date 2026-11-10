m, n = map(int, input().split())
min_prime = [0] * (n + 1)
prime = []
for i in range(2, n + 1):
	if not min_prime[i]:
		min_prime[i] = i
		prime.append(i)
	for x in prime:
		if x * i > n or x > min_prime[i]:
			break
		min_prime[x * i] = x
res, cnt = 0, 0
for i in range(m, n + 1):
	if min_prime[i] == i:
		res += i
		cnt += 1
print(f"{res / cnt:.2f}")