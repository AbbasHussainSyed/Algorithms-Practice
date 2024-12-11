# Let's solve Question 4: Design a divide-and-conquer algorithm to determine if an array is sorted in increasing order.

def is_sorted(arr):
    if len(arr) == 1:
        return arr

    start = 0
    end = len(arr)-1  # points to last position in array

    mid = (start + end) // 2  # mid = "5"
    print(mid)
    for i in range(start, mid):
        if arr[i] > arr[i+1]:
            print(arr[i], arr[i+1])
            return False

    for i in range(mid, end):
        if arr[i] > arr[i + 1]:
            print(arr[i], arr[i+1])
            return False
    return True


# Driver Program

result = is_sorted([5, 6, 7, 7, 9])
print(result)
