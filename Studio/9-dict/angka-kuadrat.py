n = int(input())

data = {}

for _ in range(n):
    key = input()
    value = int(input())

    # jika genap → kuadrat, jika ganjil → pangkat 3
    if value % 2 == 0:
        value = value ** 2
    else:
        value = value ** 3

    data[key] = value

# urutkan berdasarkan value (ascending dan descending)
asc = sorted(data.items(), key=lambda x: x[1])  # naik
desc = sorted(data.items(), key=lambda x: x[1], reverse=True)  # turun

# baris pertama: key urut berdasarkan value ascending
print(' '.join(k for k, v in asc))
# baris kedua: key urut berdasarkan value descending
print(' '.join(k for k, v in desc))