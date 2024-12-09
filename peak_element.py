# For array [1, 3, 20, 4, 1, 0]
# 20 is a peak element because it's greater than both 3 and 4
# Should return index 2

# For array [5, 10, 20, 15]
# 20 is a peak because it's greater than 10 and 15
# Should return index 2
# Note: If there are multiple peaks, we can return any one of them

def find_peak(arr, low, high):
    # Find the middle index
    mid = low + (high - low) // 2

    # Base cases for edges
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
            (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return mid

    # If left neighbor is greater, peak must be on left side
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, low, mid - 1)

    # If right neighbor is greater, peak must be on right side
    else:
        return find_peak(arr, mid + 1, high)


# Test function
def find_peak_element(arr):
    if not arr:
        return -1
    if len(arr) == 1:
        return 0
    return find_peak(arr, 0, len(arr) - 1)


# Test cases
arr1 = [1, 3, 20, 4, 1, 0]
arr2 = [5, 10, 20, 15]
print(find_peak_element(arr1))  # Should print 2 (value 20)
print(find_peak_element(arr2))  # Should print 2 (value 20)