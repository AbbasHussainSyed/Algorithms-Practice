# Find the index of target value in the rotated sorted array
# Return -1 if the target is not found
# rotated sorted array
# Input array: [6, 7, 1, 2, 3, 4, 5]
# Target: 1
# Expected output: 3 (because 2 is at index 3)

def rotated_array(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target and arr[mid]-arr[mid-1] == 1:
        return rotated_array(arr, target, low, mid-1)
    else:
        return rotated_array(arr, target, mid, high)

arr = [6, 7, 1, 2, 3, 4, 5]
result = rotated_array(arr, 1)