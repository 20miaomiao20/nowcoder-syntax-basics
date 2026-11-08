c = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
n = int(input())
a = list(map(int, input().split()))
pos = []

for s in range(30):
    flag = 1
    for i in range(n):
        if c[(s+i)%30] != a[i]:
            flag = 0
            break
    if flag:
        pos.append(s)

last = a[-1]
ans = set()
for s in pos:
    val = c[(s+n)%30]
    if val > last:
        ans.add("UP")
    else:
        ans.add("DOWN")

if len(ans) == 1:
    print(ans.pop())
else:
    print(-1)