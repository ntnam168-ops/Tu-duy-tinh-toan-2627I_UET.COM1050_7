n = int(input())
n -= n & 1
n >>= 1
print(n * (n + 1))