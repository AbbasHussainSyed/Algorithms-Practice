def jump_search(arr, target, jump_size):
    n = len(arr)

    # Step 1: Finding the block
    i = 0

    print(f"\nSearching for {target} with jump size {jump_size}")

    while (i * jump_size < n) and (arr[min(i * jump_size, n - 1)] <= target):
        print(f"Checking index {i * jump_size} with value {arr[min(i * jump_size, n - 1)]}")
        if arr[min(i * jump_size, n - 1)] == target:
            return min(i * jump_size, n - 1)
        i += 1
        if i * jump_size >= n:
            break

    # Step 2: Linear search in the block
    start = max(0, (i - 1) * jump_size)
    end = min(i * jump_size, n)

    print(f"Linear search from index {start} to {end}")

    for j in range(start, end):
        print(f"Checking index {j} with value {arr[j]}")
        if arr[j] == target:
            return j

    return -1


# Test array
arr = [2, 3, 6, 8, 10, 17, 20, 25]

# Test with different jump sizes
print("Jump size 2:", jump_search(arr, 8, 2))
print("Jump size 3:", jump_search(arr, 8, 3))
print("Jump size 4:", jump_search(arr, 8, 4))