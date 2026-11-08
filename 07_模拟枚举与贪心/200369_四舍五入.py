def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[1])
    s = data[2]
    arr = list(s)
    if '.' in arr:
        dot_pos = arr.index('.')
    else:
        dot_pos = len(arr)
    i = dot_pos + 1
    while t > 0 and i < len(arr):
        if int(arr[i]) >= 5:
            t -= 1
            carry = 1
            pos = i - 1
            while carry and pos >= 0:
                if arr[pos] == '.':
                    pos -= 1
                    continue
                new_d = int(arr[pos]) + carry
                if new_d == 10:
                    arr[pos] = '0'
                    carry = 1
                else:
                    arr[pos] = str(new_d)
                    carry = 0
                pos -= 1
            if carry:
                arr.insert(0, '1')
                dot_pos += 1
            arr = arr[:i]
            if '.' in arr:
                dot_pos = arr.index('.')
            else:
                dot_pos = len(arr)
            i = dot_pos
        i += 1
    res = ''.join(arr)
    if '.' in res:
        res = res.rstrip('0').rstrip('.')
    print(res)

if __name__ == "__main__":
    main()