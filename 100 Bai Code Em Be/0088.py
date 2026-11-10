def ucln(a, b):
	if not min(a, b):
		return max(a, b)
	a, b = max(a, b), min(a, b)
	return ucln(a % b, b)
a, b = map(int, input().split())
d = ucln(a, b)
print(a // d, "/", b // d, sep = "")