n = int(input())
ar = list(map(int, input().split()))
res = 0
for i in range(n):
	res += (1 - i & 1) * ar[i]
print(res)