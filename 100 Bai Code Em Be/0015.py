a, b, c = map(int, input().split())
if a + b + c <= max(a, max(b, c)) * 2:
	print("Day khong phai la 3 canh cua mot tam giac")
else:
	print("Day la 3 canh cua mot tam giac")
	cv = a + b + c
	p = (a + b + c) / 2
	dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	print(f"{cv:.2f}", f"{dt:.1f}")