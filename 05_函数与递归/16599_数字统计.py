L, R = map(int, input().split())
cnt = 0
for x in range(L, R + 1):
    cnt += str(x).count('2')
print(cnt)