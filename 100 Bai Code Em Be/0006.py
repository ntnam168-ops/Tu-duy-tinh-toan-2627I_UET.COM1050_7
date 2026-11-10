a, b, c = map(int, input().split())
cv = a + b + c
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"{cv:.1f}", end = " ")
print(f"{area:.3f}")