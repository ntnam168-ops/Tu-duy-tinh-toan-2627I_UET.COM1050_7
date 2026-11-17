n=int(input())
res=0
n=abs(n)
while n:
	n//=10
	res+=1
print(res)