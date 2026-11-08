T = int(input())
for _ in range(T):
    n = int(input())
    mid = n // 2
    for i in range(mid + 1):
        print(" " * (mid - i) + "*" * (2 * i + 1))
    for i in range(mid - 1, -1, -1):
        print(" " * (mid - i) + "*" * (2 * i + 1))