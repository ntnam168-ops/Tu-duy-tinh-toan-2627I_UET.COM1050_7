s = input()
x = input()
s = list(s)
for i in range(len(s) - 1, -1, -1):
	if s[i] == x:
		print(i)
		exit(0)
print(-1)