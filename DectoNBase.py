def DectoNBase(n, num):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    result = []
    while num > 0:
        result.append(symbols[num % n])
        num //= n
    return ''.join(result[::-1])
# Example usage:
n = int(input())
num = int(input())
print(DectoNBase(n, num))

# 21
# 5678
# CI8