first, second = map(int, input().split())
for i in range(first, second + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")

# Output
# 10 80
# 11 22 33 44 55 66 77