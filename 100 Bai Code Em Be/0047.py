n = int(input())
ar = list(map(int, input().split()))
x, y = [], []
for i in range(n):
	if ar[i] > 0:
		x.append(ar[i])
	elif ar[i] < 0:
		y.append(ar[i])
print(len(x), len(y))
if len(x):
	for a in x:
		print(a, end = " ")
	print()
else:
	print("-")
if len(y):
	for a in y:
		print(a, end = " ")
	print()
else:
	print("-")