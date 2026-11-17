mx,mn=0,10**18
while True:
	n=int(input())
	if n==-1:
		break
	mx=max(mx,n)
	mn=min(mn,n)
print(mx, mn)