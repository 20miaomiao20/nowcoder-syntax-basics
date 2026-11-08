s = input().strip()
cnt = 0
ok = True
for ch in s:
    if ch == 'a':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ok = False
        break
if ok and cnt == 0:
    print("Good")
else:
    print("Bad")