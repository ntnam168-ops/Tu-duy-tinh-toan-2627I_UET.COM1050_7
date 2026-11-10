a, b = map(int, input().split())
c, d = map(int, input().split())

import math
def rg(a, b):
	if a >= b:
		print(a // b, ",", sep = "", end = "")
		a %= b
	d = math.gcd(a, b)
	print(a // d, "/", b // d, sep = "")
rg(a * d + b * c, b * d)
rg(a * d - b * c, b * d)
rg(a * c, b * d)
rg(a * d, b * c)