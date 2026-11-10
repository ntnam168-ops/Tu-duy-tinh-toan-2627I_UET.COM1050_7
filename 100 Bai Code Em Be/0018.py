days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, y = map(int, input().split())
if not y % 400 or (not y % 4 and y % 100):
	days[1] += 1
print(days[m - 1])