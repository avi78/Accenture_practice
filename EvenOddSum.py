arr = []
evenArr = []
oddArr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    num = int(input(f"Enter the number at {i} index: "))
    arr.append(num)
    if i % 2 == 0:
        evenArr.append(num)
    else:
        oddArr.append(num)
oddArr.sort()
evenArr.sort()
print("Even array: ",evenArr)
print("Odd array: ", oddArr)
if len(oddArr) > 1 and len(evenArr) > 1:
    print(oddArr[-2] + evenArr[-2])
else:
    print("Not enough elements to find sum of second largest")

# Enter the size of array: 5
# Enter the number at 0 index: 3
# Enter the number at 1 index: 4
# Enter the number at 2 index: 1
# Enter the number at 3 index: 7
# Enter the number at 4 index: 9
# Even array:  [1, 3, 9]
# Odd array:  [4, 7]
# 7