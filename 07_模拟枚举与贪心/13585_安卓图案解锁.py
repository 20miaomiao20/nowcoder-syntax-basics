
skip = {
    (1, 3): 2, (3, 1): 2,
    (1, 7): 4, (7, 1): 4,
    (1, 9): 5, (9, 1): 5,
    (2, 8): 5, (8, 2): 5,
    (3, 7): 5, (7, 3): 5,
    (3, 9): 6, (9, 3): 6,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8
}

import sys

def ok(s):
    arr = list(map(int, s))
    vis = set()
    for num in arr:
        if num in vis:
            return False
        vis.add(num)
    vis.clear()
    vis.add(arr[0])
    for i in range(1, len(arr)):
        a = arr[i - 1]
        b = arr[i]
        if (a, b) in skip:
            mid = skip[(a, b)]
            if mid not in vis:
                return False
        vis.add(b)
    return True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if ok(line):
        print("YES")
    else:
        print("NO")