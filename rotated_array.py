# Find the index of target value in the rotated sorted array
# Return -1 if the target is not found
# rotated sorted array
# Input array: [6, 7, 1, , 3, 4, 5]
# Target: 2
# Expected output: 3 (because 2 is at index 3)

def rotated_array(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
