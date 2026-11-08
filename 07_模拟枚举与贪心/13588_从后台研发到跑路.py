import sys

def main():
    s = sys.stdin.read()
    res = []
    i = 0
    n = len(s)
    in_str = False
    quote = ''
    escape = False
    while i < n:
        c = s[i]
        if escape:
            res.append(c)
            escape = False
            i += 1
            continue
        if c == '\\':
            res.append(c)
            escape = True
            i += 1
            continue
        if in_str:
            res.append(c)
            if c == quote:
                in_str = False
            i += 1
            continue
        if c in ('"', "'"):
            res.append(c)
            in_str = True
            quote = c
            i += 1
            continue
        if c == '/' and i + 1 < n and s[i+1] == '*':
            # 开始尝试读注释
            j = i + 2
            found = False
            while j + 1 < n:
                if s[j] == '*' and s[j+1] == '/':
                    found = True
                    j += 2
                    break
                j += 1
            if found:
                i = j
            else:
                # 没有找到 */，保留这两个字符
                res.append('/')
                res.append('*')
                i += 2
            continue
        res.append(c)
        i += 1
    print(''.join(res), end='')

if __name__ == "__main__":
    main()