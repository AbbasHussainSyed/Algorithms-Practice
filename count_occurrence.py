import first_occurrence
import last_occurrence


def count_occurrence(arr, val):
    first = first_occurrence(arr, val, 0, len(arr) - 1)
    last = last_occurrence(arr, val, 0, len(arr) - 1)

    if first == -1:
        return -1

    return last - first + 1

arr = [1,2,]