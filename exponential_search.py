# Problem: Implement exponential search to find target element in a sorted array
# Example array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# If target = 12, return its index (5)
# If target not found, return -1

def exponential_search(arr, target, low, high):
        if low > high:
                return -1

        
        if arr[mid] == target:
                return mid
