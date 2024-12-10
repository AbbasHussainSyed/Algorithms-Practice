# dynamic programming tribonacci algorithm

def tribonacci(n):
    M = [0, 0, 1]

    for i in range(3, n + 1):
        M.append(M[i - 1] + M[i - 2] + M[i - 3])

    return M[n]


result = tribonacci(5)
print(result)
