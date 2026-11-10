a, b = map(int, input().split())
# x = -b / a
if not a:
	if not b:
		print("Vo so ngihem")
	else:
		print("Vo ngihem")
else:
	print("Nghiem cua phuong trinh:", -b / a)