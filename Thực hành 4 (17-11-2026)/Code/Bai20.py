n=int(input())
res=0
a=[2,3,5,7]
while n:
	if n%10 in a:
		res+=1
	n//=10
print(res)