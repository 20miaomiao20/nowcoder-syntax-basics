import sys

def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

for line in sys.stdin:
    n = int(line.strip())
    print_pyramid(n)