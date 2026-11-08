import sys


def next_permutation(nums: list[int]) -> bool:
    """原地改成字典序的下一个排列；已经是最后一个排列时返回 False。"""
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return True


def main() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    lines = []
    while True:
        lines.append(" ".join(map(str, arr)))
        if not next_permutation(arr):
            break
    sys.stdout.write("\n".join(lines) + "\n")   # 一次性输出，比循环 print 快得多


if __name__ == "__main__":
    main()