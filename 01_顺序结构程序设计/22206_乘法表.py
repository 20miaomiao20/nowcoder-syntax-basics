for i in range(1, 10):
    line = []
    for j in range(1, i + 1):
        res = i * j
        line.append(f"{j}*{i}={res:2d}")
    print(' '.join(line))