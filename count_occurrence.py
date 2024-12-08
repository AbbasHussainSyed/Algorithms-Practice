import first_occurrence
import  last_occurrence

def count_occurrence(arr, val):

    first = first_occurrence(arr, val, low, high)
    last = last_occurrence(arr, val, low, high)

    if first == -1:
        return -1

    return last-first+1