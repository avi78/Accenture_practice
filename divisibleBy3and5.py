def Calculate(m, n):
    return sum(i for i in range(m, n + 1) if i % 3 == 0 and i % 5 == 0)
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
print(Calculate(m, n))

# Enter the value of m: 100
# Enter the value of n: 160
# 510