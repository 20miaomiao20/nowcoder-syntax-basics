n, x = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    s = str(i)
    cnt += s.count(str(x))
print(cnt)