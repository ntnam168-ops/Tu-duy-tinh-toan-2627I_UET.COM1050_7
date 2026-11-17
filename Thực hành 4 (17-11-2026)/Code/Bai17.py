n=int(input())
res=0
n=abs(n)
while n:
	res+=n%10
	n//=10
print(res)