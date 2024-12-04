def algorithm1(n):
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(j):
                print(k)
                total = total + 1
    return total


result = algorithm1(4)
print(result)

