# Given an array A of n integers and a value x, count how many elements in A are strictly greater than x.
# Use a divide-and-conquer algorithm to solve the problem

def count_elements(arr, x):
    if len(arr)==0:
        return 0