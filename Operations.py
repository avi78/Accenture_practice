def operationChoices(c, a, b):
    operations = {
        1: a + b,
        2: a - b,
        3: a * b,
        4: a // b if b != 0 else 'Error: Division by zero'
    }
    return operations.get(c, 'Invalid choice')
c, a, b = map(int, input().split())
print(operationChoices(c, a, b))

# 1 12 16
# 28