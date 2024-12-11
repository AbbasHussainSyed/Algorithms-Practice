# Input array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Target = 7
# Should return index 6

def ternary_search(arr, target, low, high):
    if low > high:
        return -1

    # Calculate the two midpoints correctly
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    # Found at either midpoint
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    # Target in left third
    if target < arr[mid1]:
        return ternary_search(arr, target, low, mid1 - 1)

    # Target in right third
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, high)

    # Target in middle third
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


# Test the function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ternary_search(arr, 7, 0, len(arr) - 1))  # Should print 6
