ar = list(map(int, input().split()))
ar.sort()
if len(ar) < 2:
	print('-')
else:
	print(ar[-2])