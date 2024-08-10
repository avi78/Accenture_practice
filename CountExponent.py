def maxExponents(a, b):
    def countExponents(i):
        count = 0
        while i % 2 == 0 and i != 0:
            count += 1
            i //= 2
        return count
    return max(range(a, b + 1), key=countExponents)
a, b = map(int, input().split())
print(maxExponents(a, b))

# Explanation:
# Exponents of 2 in:
# 7-0
# 8-3
# 9-0
# 10-1
# 11-0
# 12-2
# Hence maximum exponent if two is of 8.
# Output-
# 7 12
# 8