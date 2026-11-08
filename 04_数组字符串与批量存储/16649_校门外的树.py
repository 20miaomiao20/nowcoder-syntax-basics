L, M = map(int, input().split())
trees = [True] * (L + 1)
for _ in range(M):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        trees[i] = False
print(sum(trees))