def MaxInArray(arr):
    if not arr:
        return
    max_value = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    print(max_value)
    print(max_index)

# Example usage
MaxInArray([23, 45, 82, 27, 66, 12, 78, 13, 71, 86])
