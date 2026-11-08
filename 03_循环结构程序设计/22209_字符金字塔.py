ch = input().strip()
end = ord(ch)
start = ord('A')
n = end - start

for i in range(n + 1):
    c = chr(start + i)
    print(" " * (n - i) + "".join(chr(start + k) for k in range(i + 1)) + "".join(chr(start + k) for k in range(i - 1, -1, -1)))