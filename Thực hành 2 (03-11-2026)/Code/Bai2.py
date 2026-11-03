a, b = map(float, input().split())
pi = 3.14
res = a * b - a ** 2 / 4 * pi
print(round(res, 2))