s = input()
res = 0
for k in s:
	res += ord(k) - ord('0')
res %= 10
print(res)
print("may man" if res == 9 else "chua may man")