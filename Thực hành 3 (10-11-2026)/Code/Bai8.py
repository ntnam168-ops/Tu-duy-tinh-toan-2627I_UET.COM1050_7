a, b, m, c, d, n = map(int, input().split())
f = c / a
a *= f
b *= f
m *= f
y = (n - m) / (d - b)
x = (m - b * y) / a
print("Nghiem cua phuong trinh tuyen tinh:", x, y)