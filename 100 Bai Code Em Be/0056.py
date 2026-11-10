import sys
ar = []
for l in sys.stdin:
	ar.append(int(l))
ar.sort()
if len(ar) < 3:
	print('-')
else:
	print(ar[2])