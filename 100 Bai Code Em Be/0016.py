a, b = map(int, input().split())
s = (a + b * 2) / 3
print(f"{s:.1f}")
if s >= 8:
	print("Gioi")
elif s >= 6.5:
	print("Kha")
elif s >= 5:
	print("Trung binh")
elif s >= 3.5:
	print("Yeu")
else:
	print("Kem")