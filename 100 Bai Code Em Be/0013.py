a, b, c = map(int, input().split())
if a == b and b == c:	
	print("=")
else:
	print(max(a, max(b, c)))