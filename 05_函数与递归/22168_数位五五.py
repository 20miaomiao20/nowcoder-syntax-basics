def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

x, y = map(int, input().split())
l = min(x, y)
r = max(x, y)
cnt = 0
for i in range(l, r + 1):
    if sum_digit(i) % 5 == 0:
        cnt += 1
print(cnt)