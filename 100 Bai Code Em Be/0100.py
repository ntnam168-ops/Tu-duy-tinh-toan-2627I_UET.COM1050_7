n = int(input())
ar = list(map(int, input().split()))
mx = max(ar)
print(mx, end = " ")
for i in range(n):
	if ar[i] == mx:
		print(i, end = " ")
print()
mx = min(ar)
print(mx, end = " ")
for i in range(n):
	if ar[i] == mx:
		print(i, end = " ")