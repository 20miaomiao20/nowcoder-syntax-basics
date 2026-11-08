n = int(input())
a = list(map(int, input().split()))
a.sort()
ok = False
x = y = z = 0
for i in range(2, n):
    if a[i-2] + a[i-1] > a[i]:
        x, y, z = a[i-2], a[i-1], a[i]
        ok = True
        break
if ok:
    print(x, y, z)
else:
    print("No solution")