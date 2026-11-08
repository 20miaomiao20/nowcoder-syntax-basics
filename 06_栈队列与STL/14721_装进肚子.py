def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+n]))
    idx += n
    B = list(map(int, data[idx:idx+n]))
    idx += n
    total = sum(B)
    diff = [A[i] - B[i] for i in range(n)]
    diff.sort(reverse=True)
    for i in range(K):
        total += diff[i]
    print(total)

if __name__ == "__main__":
    main()