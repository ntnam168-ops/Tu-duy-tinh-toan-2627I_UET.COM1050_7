a=int(input())
res=0
for i in range(1,int(a**0.5)+1):
	if a%i==0:
		res+=i
		if i*i!=a:
			res+=a//i
if a*2==res:
	print("la so hoan hao")
else:
	print("khong phai so hoan hao")