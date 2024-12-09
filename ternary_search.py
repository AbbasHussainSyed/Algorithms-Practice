# Input array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Target = 7
# Should return index 6

def ternary_search(arr, val, low, high):
    if low > high:
        return -1

    mid1 = low + (high - low) // 1/2
    mid2 = low + ()