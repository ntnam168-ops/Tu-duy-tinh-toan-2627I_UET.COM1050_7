a, b, c = map(int, input().split())
if a + b + c <= max(a, max(b, c)) * 2:
	print("Khong la ba canh cua mot tam giac")
	exit(0)

if a == b and b == c:
	print("Tam giac deu")
elif a == b or b == c or c == a:
	print("Tam giac can")
elif a * a + b * b + c * c == max(a, max(b, c)) ** 2 * 2:
	print("Tam giac vuong")
else:
	print("Tam giac thuong")

p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5;

print("Dien tich hinh tam giac:", area)
print("Chu vi hinh tam giac", a + b + c)