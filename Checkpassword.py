def CheckPassword(s):
    # Check length and starting character
    if len(s) < 4 or s[0].isdigit():
        return 0
    
    # Initialize flags
    has_digit = any(ch.isdigit() for ch in s)
    has_upper = any(ch.isupper() for ch in s)
    
    # Check for space or slash
    if ' ' in s or '/' in s:
        return 0
    
    # Final checks
    if not has_digit or not has_upper:
        return 0
    
    return 1

# Example usage:
password1 = "aA1_67"
password2 = "a987 abC012"

print("Output 1:", CheckPassword(password1))  # Output: 1
print("Output 2:", CheckPassword(password2))  # Output: 0
