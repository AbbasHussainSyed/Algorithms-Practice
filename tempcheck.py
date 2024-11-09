temperatures = [18, 22, 30, 35]
i = 0
while i < len(temperatures):
    if temperatures[i] > 20:
        print("Temperature", temperatures[i], "is greater than 20.")
        continue
    print("Temperature", temperatures[i], "might require a jacket.")
    i += 1