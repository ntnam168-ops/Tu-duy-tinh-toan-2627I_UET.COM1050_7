s = input()
s = list(s)
for i in range(len(s)):
	if s[i] != " ":
		if not i or s[i - 1] == " ":
			s[i] = s[i].upper()
s = "".join(s)
print(s)