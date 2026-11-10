import math
a, b = map(int, input().split())
d = math.gcd(a, b)
print(a // d, "/", b // d, sep = "")