n = int(input())
ar = list(map(int, input().split()))
res = 0
for i in range(n):
	res += ar[i] * (1 - ar[i] & 1)
print(res)