import sys
ar = []
for l in sys.stdin:
	ar.append(int(l))
ar.sort()
ar = set(ar)
print(len(ar))