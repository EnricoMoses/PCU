data = [['jojo', 90], ['jiji', 60], ['jaja', 10], ['koko', 80], ['jj', 61]]

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j][1] < data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)