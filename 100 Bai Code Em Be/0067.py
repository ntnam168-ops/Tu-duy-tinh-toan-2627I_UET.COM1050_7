s = input()
for i in range(len(s) - 1, -1, -1):
	if s[i] != ' ':
		print(s[:i + 1])
		exit(0)