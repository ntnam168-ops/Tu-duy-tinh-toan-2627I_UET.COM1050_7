n = int(input())
ar = list(map(int, input().split()))
res, cnt = 0, 0
for i in range(n):
	if ar[i] % 2 == 0:
		res += ar[i];
		cnt += 1
if not cnt:
	print('-')
else:
	print(f"{res / cnt :.2f}")