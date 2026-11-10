def cv(a, b, c):
	return a + b + c
def dt(a, b, c):
	p = (a + b + c) / 2
	return (p * (p - a) * (p - b) * (p - c)) ** 0.5
a, b, c = map(int, input().split())
print(f"{cv(a, b, c):.1f}", f"{dt(a, b, c):.3f}")