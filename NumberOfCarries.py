def NumberOfCarries(n1, n2):
    # Pad the shorter number with leading zeros
    max_len = max(len(n1), len(n2))
    n1 = n1.zfill(max_len)
    n2 = n2.zfill(max_len)
    carry = 0
    count = 0
    for i in range(max_len - 1, -1, -1):
        total = int(n1[i]) + int(n2[i]) + carry
        if total >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
    return count
n1 = input()
n2 = input()
print(NumberOfCarries(n1, n2))

# Example:
# Input
# Num 1: 451
# Num 2: 349
# Output
# 2
# Explanation:
# Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

# Sample Input
# Num 1: 23
# Num 2: 563
# Sample Output
# 0