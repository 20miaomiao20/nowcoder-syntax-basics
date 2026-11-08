from functools import cmp_to_key

def cmp(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

n = int(input())
arr = input().split()
arr.sort(key=cmp_to_key(cmp))
res = ''.join(arr)
print(res)