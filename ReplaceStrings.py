def swap(user_input, str1, str2):
    if user_input is None:
        return 'Null'
    return user_input.replace(str1, '#').replace(str2, str1).replace('#', str2)
user_input = input()
str1, str2 = input().split()
print(swap(user_input, str1, str2))

# apples
# a p
# paales