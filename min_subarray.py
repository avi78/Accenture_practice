def subarray(arr,k):
    if arr is None or len(arr)<k:
        return None
    min_sum = float('inf')
    min_subarray = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        current_sum = sum(subarray)
        if(current_sum< min_sum):
            min_sum = current_sum
            min_subarray = subarray
    return min_subarray
arr = [3,2,1,-4,6,3,1]
k=3
print(subarray(arr,k))

# output - [2, 1, -4]