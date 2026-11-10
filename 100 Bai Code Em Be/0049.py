n = int(input())
ar = list(map(int, input().split()))
d = max(ar)
for i in range(n):
	if ar[i] == d:
		print(d, i)
		exit(0)