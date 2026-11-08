n, k, m = map(int, input().split())
lst = list(range(n))
pos = k
while len(lst) > 1:
    pos = (pos + m - 1) % len(lst)
    lst.pop(pos)
print(lst[0])