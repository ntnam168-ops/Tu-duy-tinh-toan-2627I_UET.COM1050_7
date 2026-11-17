n=int(input())
k=int((2*n)**0.5)
if k*(k+1)//2>=n:
	k-=1
print(k)