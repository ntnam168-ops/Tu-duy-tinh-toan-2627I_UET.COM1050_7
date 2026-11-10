n = int(input())
def f(n):
	if n < 2:
		return "No"
	d = int(n ** 0.5)
	for i in range(2, d + 1):
		if not n % i:
			return "No"
	return "Yes"
print(f(n))