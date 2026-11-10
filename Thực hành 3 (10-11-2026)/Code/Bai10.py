def dis(a, b, c, d):
	return ((a - c) ** 2 + (b - d) ** 2) ** 0.5

Ix, Iy, r = map(float, input().split())
x, y = map(float, input().split())
if dis(Ix, Iy, x, y) <= r:
	print("Diem nay nam trong duong tron")
else:
	print("Diem nay khong nam trong duong tron")