n = int(input())
ar = []
for i in range(n):
	ar.append(int(input()))
mp = {}
for i in ar:
	mp[i] = mp.get(i, 0) + 1
for i in ar:
	if mp[i]:
		print(i, mp[i])
		mp[i] = 0