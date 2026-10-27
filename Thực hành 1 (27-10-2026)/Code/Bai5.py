c = input()
if c == "A":
	print("Khong ton tai")
else:
	print(chr(ord(c) - ord('A') + ord('a') - 1))