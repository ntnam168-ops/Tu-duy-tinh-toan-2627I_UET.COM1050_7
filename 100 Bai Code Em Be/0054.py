ar = list(map(int, input().split()))
ar.sort()
ar = ar[::-1]
for i in ar:
	if i < 0:
		print(i)
		exit(0)
print('-')