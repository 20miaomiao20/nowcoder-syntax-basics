word_map = {
    "zero": "0",
    "two": "2",
    "four": "4",
    "six": "6",
    "nine": "9"
}
words = ["zero", "four", "nine", "two", "six"]

def solve(s):
    res = []
    i = 0
    n = len(s)
    while i < n:
        matched = False
        for w in words:
            lw = len(w)
            if i + lw <= n and s[i:i+lw] == w:
                res.append(word_map[w])
                i += lw
                matched = True
                break
        if matched:
            continue
        if s[i] in "02469":
            res.append(s[i])
        i += 1
    return ''.join(res)

def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        print(solve(input[i]))

if __name__ == "__main__":
    main()