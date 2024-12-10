# dynamic programming algorithm for coins change

def coins_change(coin):
    M = [0, 1, 2, 3, 4, 1, 2, 1]

    for i in range(8, coin):
        coins = min(M[i - 1] + 1, M[i - 5] + 1, M[i - 7] + 1)
    return coins
