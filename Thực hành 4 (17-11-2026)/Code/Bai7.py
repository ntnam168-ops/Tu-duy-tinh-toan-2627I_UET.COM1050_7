a=int(input())
res=0
for i in range(1,int(a**0.5)+1):
	if a%i==0:
		res+=1
		if i*i!=a:
			res+=1
print(res)