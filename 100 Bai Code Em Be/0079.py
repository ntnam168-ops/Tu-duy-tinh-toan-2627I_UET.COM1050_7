s = input()
s = s.lower()
mp = {}
res = 0
for k in s:
	mp[k] = mp.get(k, 0) + 1
	res = max(res, mp[k])
for k in s:
	if mp[k] == res:
		print(k, ":", res, sep = "")
		exit(0)