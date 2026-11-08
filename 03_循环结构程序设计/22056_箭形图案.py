# NC22056 箭形图案（多组输入读到 EOF）
# 共 2n+1 行，第 k 行：2*|n-k| 个空格 + (n+1-|n-k|) 个星号
import sys

for line in sys.stdin:
    if not line.strip():
        continue
    n = int(line)
    for k in range(2 * n + 1):
        gap = abs(n - k)
        print(" " * (2 * gap) + "*" * (n + 1 - gap))
