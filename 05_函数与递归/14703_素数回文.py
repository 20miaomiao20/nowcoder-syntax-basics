# NC14703 素数回文
# 回文数 = 正序 + 倒序去掉最后一位：13 -> 131，127 -> 12721（不是 31！）
# 回文数能到 10^17 量级，试除法会超时，改用 Miller-Rabin 判素数
import sys


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


s = sys.stdin.read().strip()
pal = int(s + s[::-1][1:])
print("prime" if is_prime(pal) else "noprime")
