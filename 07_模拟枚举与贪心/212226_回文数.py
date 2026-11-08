# NC212226 回文数：给每个数码的出现次数，构造最小的回文数（不能有前导 0）
# 奇数个数的数码最多只能有 1 个（放在正中间），否则无解
cnt = list(map(int, input().split()))

odd_list = []
for d in range(10):
    if cnt[d] % 2 == 1:
        odd_list.append(d)

if len(odd_list) > 1:
    print(-1)
else:
    mid = ""
    if len(odd_list) == 1:
        mid = str(odd_list[0])
        cnt[odd_list[0]] -= 1

    left = []
    found = False
    # 首位必须是非零数字，取最小的那个，才能避免前导 0
    for d in range(1, 10):
        if cnt[d] >= 2:
            left.append(str(d))
            cnt[d] -= 2
            found = True
            break

    if not found:
        # 没有非零的成对数字：只有"单个数字"（例如只有一个 0）才合法
        if mid != "" and sum(cnt) == 0:
            print(mid)
        else:
            print(-1)
    else:
        for d in range(10):
            left.append(str(d) * (cnt[d] // 2))
        s = ''.join(left)
        print(s + mid + s[::-1])
