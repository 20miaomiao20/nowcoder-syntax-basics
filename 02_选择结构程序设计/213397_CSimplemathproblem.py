x, y = map(int, input().split())
if y % x == 0:
    z = x + y
else:
    z = y - x
print(z)
