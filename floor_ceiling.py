"""arr = [1, 2, 4, 8, 10, 12, 14]
target = 5

floor = 4   (largest number ≤ 5)
ceiling = 8 (smallest number ≥ 5)"""

def floor_ceiling(arr, target, low, high):
    if len(arr) == 1:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] <= target:
        return mid
    if arr[mid] >= target:
        return 