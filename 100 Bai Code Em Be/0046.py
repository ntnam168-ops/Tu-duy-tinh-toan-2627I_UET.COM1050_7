n, x = map(int, input().split())
ar = list(map(int, input().split()))
for i in range(n):
	if ar[i] == x:
		print("Yes", i, sep = "\n")
		exit(0)
print("No")