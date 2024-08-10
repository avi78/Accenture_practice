num = int(input())
sum = 0
for i in range(1,11):
    val = num * i
    print(val, end = " ")
    sum += val
print()
print(sum)

# num = int(input())
# total_sum = sum(num * i for i in range(1, 11))
# print(" ".join(str(num * i) for i in range(1, 11)))
# print(total_sum)

# num = int(input())
# multiples = [num * i for i in range(1, 11)]
# print(*multiples)
# print(sum(multiples))

# 7
# 7 14 21 28 35 42 49 56 63 70 
# 385