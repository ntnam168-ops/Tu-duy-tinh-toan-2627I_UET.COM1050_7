s = input()
a = input()
b = input()

s = s[12:]
a = int(a[20:])
b = int(b[18:])

def f(val):
	x = [0, 50, 100, 200, 300, 400]
	y = [1984, 2050, 2380, 2998, 3350, 3460]
	res = 0
	for i in range(1, 6):
		if val <= x[i]:
			return ((val - x[i - 1]) * y[i - 1]) + res
		res += (x[i] - x[i - 1]) * y[i - 1]
	return res + (val - x[-1]) * y[-1]

res  = f(b - a)
res *= 1.08

print("Ho va ten:", s)
print("Tien phai tra la:", round(res))