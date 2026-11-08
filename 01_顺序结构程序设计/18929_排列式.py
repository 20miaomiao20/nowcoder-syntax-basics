def is_valid(a, b):
    product = a * b
    all_str = str(a) + str(b) + str(product)
    if len(all_str) != 9:
        return False
    if '0' in all_str:
        return False
    if len(set(all_str)) == 9:
        return True
    return False


answer_list = []

for a in range(1, 200):
    for b in range(a + 1, 2000):
        if is_valid(a, b):
            p = a * b
            answer_list.append((p, a, b))

answer_list.sort(key=lambda item: (item[0], item[1]))

for num, x, y in answer_list:
    print(f"{num} = {x} x {y}")