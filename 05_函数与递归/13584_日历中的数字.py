import calendar

def count_digit(y, m, x):
    cnt = 0
    s = str(x)
    days = calendar.monthrange(y, m)[1]
    for d in range(1, days + 1):
        date_str = f"{y}-{m:02d}-{d:02d}"
        cnt += date_str.count(s)
    return cnt

while True:
    try:
        y, m, x = map(int, input().split())
        print(count_digit(y, m, x))
    except EOFError:
        break