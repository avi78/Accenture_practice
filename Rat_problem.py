def calculate(r,unit,arr,n):
    if arr is None or n == 0:
        return -1
    totalFoodRequired = r * unit
    foodTillNow = 0
    for house in range(n):
        foodTillNow += arr[house]
        if foodTillNow >= totalFoodRequired:
            return house + 1
    return 0
    
r = 7
unit = 2
arr = [2,8,3,5,7,4,1,2]
n = 8
print(calculate(r,unit,arr,n))

# output - 4