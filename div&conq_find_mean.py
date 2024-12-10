# Find the mean of the values in an array A of length n using a divide and conquer approach.

def find_mean(arr):
    if len(arr) == 1:
        return arr[0], 1
    if len(arr) == 2:
        return arr[0] + arr[1] // 2, 2

    mid = len(arr) // 2

    left_mean, left_count = arr[:mid]//2, 