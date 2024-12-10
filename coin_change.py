# dynamic programming algorithm for coins change

def coins_change(coin):
    M = [0, 1, 2, 3, 4, 1, 2, 1] # base case coins needed for each amount till 7

    M.extend([float('inf')]*(coin-7))

    for i in range(8, coin+1):
        M[i] = min(M[i - 1] + 1, M[i - 5] + 1, M[i - 7] + 1)
    return M[coin]


result = coins_change(11)
print(result)