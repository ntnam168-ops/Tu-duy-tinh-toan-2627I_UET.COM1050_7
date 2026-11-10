def cp(n):
	d = int(n ** 0.5)
	return d * d == n
n = int(input())
print("Yes" if cp(n) else "No")