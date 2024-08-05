def OperationsBinaryString(s):
    if s is None or len(s) == 0:
        return -1
    
    current_result = int(s[0])  # Start with the first binary digit
    i = 1
    
    while i < len(s):
        operation = s[i]
        operand = int(s[i + 1])
        
        if operation == 'A':
            current_result &= operand
        elif operation == 'B':
            current_result |= operand
        elif operation == 'C':
            current_result ^= operand
        
        i += 2
    
    return current_result

# Example usage:
input_str = "1C0C1C1A0B1"
print(OperationsBinaryString(input_str))  # Output: 1

input_str = "0C1A1B1C1C1B0A0"
print(OperationsBinaryString(input_str))  # Output: 0
