def FindAutoCount(n):
    if not n:
        return 0
    digit_count = [0] * 10
    for char in n:
        digit_count[int(char)] += 1
    if all(int(n[i]) == digit_count[i] for i in range(len(n))):
        return len(set(n))
    return 0
print(FindAutoCount('1210'))