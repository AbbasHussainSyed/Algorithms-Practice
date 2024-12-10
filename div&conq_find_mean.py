# Find the mean of the values in an array A of length n using a divide and conquer approach.

def find_mean(arr):
    if len(arr) == 1:
        return arr[0], 1
    if len(arr) == 2:
        return arr[0] + arr[1] // 2, 2

    mid = len(arr) // 2

    left_mean, left_count = find_mean(arr[:mid])
    right_mean, right_count = find_mean(arr[mid:])

    total_count = left_count + right_count

    combined_mean = (left_mean * left_count + right_mean * right_count) / total_count

    return combined_mean, total_count


arr = [2, 4, 6, 8, 10]
result = find_mean(arr)
print(result)
