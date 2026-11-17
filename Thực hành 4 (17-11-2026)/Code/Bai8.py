import math
a,b=map(int,input().split())
a=math.gcd(a,b)
ar=[]
for i in range(1,int(a**0.5)+1):
	if a%i==0:
		ar.append(i)
		if i*i!=a:
			ar.append(a//i)
ar.sort()
for x in ar:
	print(x,end=" ")