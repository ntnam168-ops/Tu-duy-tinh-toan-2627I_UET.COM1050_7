n = int(input())
x = [50, 100, 200]
y = [600, 800, 1100]
res = 0
for i in range(3):
	if n >= x[i]:
		res += (x[i] - (0 if not i else x[i - 1])) * y[i]
	else:
		res += (n - (0 if not i else x[i - 1])) * y[i]
		break
if n > x[-1]:
	res += (n - x[-1]) * 1500
print(res)