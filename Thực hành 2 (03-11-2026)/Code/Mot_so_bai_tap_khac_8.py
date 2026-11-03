n = int(input())
print("Nam nhuan" if n % 400 == 0 or (n % 4 == 0 and n % 100) else "Khong phai nam nhuan")