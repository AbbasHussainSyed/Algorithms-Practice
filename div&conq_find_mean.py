# Find the mean of the values in an array A of length n using a divide and conquer approach.

def find_mean(arr):
    if len(arr) == 1:
        return arr[0], 1
    el