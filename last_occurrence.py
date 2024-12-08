#  modified binary search algorithm to find last occurrence

def last_occurrence(arr, val, low, high):
    #  base case
    if low > high:
        return "value not in array"

    mid = low + (high - low) // 2

    if arr[mid] == val:
        if arr[mid] == high or arr[mid + 1] > val:
            return mid
        else:
            return last_occurrence(arr, val, mid + 1, high)
    elif arr[mid] > val:
        return last_occurrence(arr, val, low, mid - 1)
    else:
        return last_occurrence(arr, val, mid + 1, high)


arr = [2, 4, 4, 5, 6, 6]
result = last_occurrence(arr, 3, low=0, high=len(arr) - 1)
print(result)
