# Problem: Implement exponential search to find target element in a sorted array
# Example array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# If target = 14, return its index (6)
# If target not found, return -1

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return 
