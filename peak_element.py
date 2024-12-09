# For array [1, 3, 20, 4, 1, 0]
# 20 is a peak element because it's greater than both 3 and 4
# Should return index 2

# For array [5, 10, 20, 15]
# 20 is a peak because it's greater than 10 and 15
# Should return index 2

# Note: If there are multiple peaks, we can return any one of them

def peak_element(arr, peak, low, high):
    if len(arr) == 1:
        return 0

    mid = low + (high - low) // 2

        
