n = int(input())
ar = list(map(int, input().split()))
ar.sort()
for i in range(n):
	print(ar[i], end = " ")