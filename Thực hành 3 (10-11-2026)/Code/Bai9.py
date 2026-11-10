s = int(input())
h = s // 3600
s %= 3600
m = s // 60
s %= 60
print(h, ":", m, ":", s)