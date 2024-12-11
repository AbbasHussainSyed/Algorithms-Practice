# given an array find the longest subsequence - dynamic programming
# example arr = [3,10,2,1,20] the longest subsequence is 3

def longest_subsequence(arr):
    M = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                print(i)
                M[i] = max(M[i], M[j]+1)
    return max(M)


result = longest_subsequence([3, 10, 2, 1, 20])
print(result)