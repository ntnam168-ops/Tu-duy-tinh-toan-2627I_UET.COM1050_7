n = int(input())
ar = list(map(int, input().split()))
x = []
for i in range(n):
	if not ar[i] % 5:
		x.append(ar[i])
for i in x:
	print(i, end = " ")
print()
print(sum(x))