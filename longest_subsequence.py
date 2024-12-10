# given an array find the longest subsequence
# example arr = [3,10,2,1,20] the longest subsequence is 3

def longest_subsequence(arr):
    M = [1] * len(arr)

    for i in range(0, len(arr)):
        for j in range(1, i):
            if arr[j] > arr[i]:
                M[i] = max(M[i], M[j]+1)
    return M


result = longest_subsequence([3, 10, 2, 1, 20])
print(result)