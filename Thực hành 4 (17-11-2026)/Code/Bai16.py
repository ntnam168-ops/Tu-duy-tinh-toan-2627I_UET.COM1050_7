n=int(input())
res,l=0,0
n=abs(n)
while n:
	res+=1
	l+=n&1
	n//=10
print(l,res-l)