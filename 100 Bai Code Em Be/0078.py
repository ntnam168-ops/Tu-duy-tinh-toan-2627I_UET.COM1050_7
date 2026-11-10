s = input()
s = s.lower()
mp = {}
for k in s:
	mp[k] = mp.get(k, 0) + 1
for k in s:
	if mp[k]:
		print(k, ":", mp[k], sep = "", end = " ")
		mp[k] = 0