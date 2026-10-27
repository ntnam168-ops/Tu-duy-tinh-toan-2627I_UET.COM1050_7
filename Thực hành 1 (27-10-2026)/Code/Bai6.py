a, b, c = map(int, input().split())
if (a + b > c) and (b + c > a) and (c + a > b):
	p = (a + b + c) / 2
	res = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	print(round(res, 1))
else:
	print("Khong phai 3 canh cua tam giac")