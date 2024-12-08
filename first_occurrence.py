#  modified binary search algorithm to find the first index in the array
def first_occurrence(arr, val, low, high):

    if low > high:
        return "value not in array"
