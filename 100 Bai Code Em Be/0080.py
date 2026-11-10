s = input()
x = input()
s = list(s)
for i in range(len(s)):
	if s[i] == x:
		print(i)
		exit(0)
print(-1)