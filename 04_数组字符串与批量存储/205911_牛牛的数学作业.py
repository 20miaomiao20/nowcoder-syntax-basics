# NC205911：求每张试卷的极差和方差（方差保留 3 位小数）
# 直接用浮点数算方差会在末位抖动，这里用整数分子 (n*Σa² - (Σa)²) / n²，
# 再用 Decimal 四舍五入到 3 位，保证 86075.959 这种结果稳定正确
import sys
from decimal import Decimal, ROUND_HALF_UP


def main():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    out = []
    for _ in range(T):
        n = int(data[ptr])
        ptr += 1
        s1 = 0
        s2 = 0
        mx = -float('inf')
        mn = float('inf')
        for __ in range(n):
            x = int(data[ptr])
            ptr += 1
            s1 += x
            s2 += x * x
            if x > mx:
                mx = x
            if x < mn:
                mn = x
        diff = mx - mn
        var = Decimal(n * s2 - s1 * s1) / Decimal(n * n)
        var = var.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
        out.append(f"{diff} {var}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
