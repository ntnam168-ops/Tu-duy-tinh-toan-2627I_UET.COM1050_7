n = int(input())
ar = []
for i in range(n):
	ar.append(int(input()))
mp = {}
res = 0
for i in ar:
	mp[i] = mp.get(i, 0) + 1
	res = max(res, mp[i])
for i in ar:
	if mp[i] == res:
		print(i, mp[i])
		exit(0)