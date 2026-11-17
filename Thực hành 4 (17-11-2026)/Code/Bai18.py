n=int(input())
while n%3==0:
	n//=3
print("Co" if n==1 else "Khong")