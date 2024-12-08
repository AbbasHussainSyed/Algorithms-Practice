#  modified binary search algorithm to find the first index in the array
def first_occurrence(arr, val, low, high):
    #  base case
    if low > high:
        return "value not in array"

    mid = low + (high-low) // 2

    if arr[mid] == val:
        if arr[mid] == 0 or arr[mid-1] < val:
            return arr[mid]
        else:
            return first_occurrence(arr, val, low, mid-1)
