a, b, c = map(int, input().split())

# delta = b ^ 2 - 4ac
# ans = (-b +- sqrt(delta)) / (2a)

delta = b ** 2 - 4 * a * c
if delta < 0:
	print("Phuong trinh vo nghiem")
elif delta == 0:
	print("Phuong trinh co nghiem duy nhat:", -b / (2 * a))
else:
	print("Phuong trinh co 2 nghiem:")
	print("Nghiem 1:", (-b - delta ** 0.5) / (2 * a))
	print("Nghiem 2:", (-b + delta ** 0.5) / (2 * a))