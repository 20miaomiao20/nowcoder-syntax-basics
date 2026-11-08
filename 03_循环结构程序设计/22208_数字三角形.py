n = int(input())
cnt = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{cnt:4d}", end="")
        cnt += 1
    print()