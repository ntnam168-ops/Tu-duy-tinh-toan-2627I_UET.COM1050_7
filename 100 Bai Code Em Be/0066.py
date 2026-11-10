s = input()
for i in range(len(s)):
	if s[i] != ' ':
		print(s[i:])
		exit(0)