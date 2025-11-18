n = int(input())

data = {}

for _ in range(n):
    key = input()
    value = input()
    value.lower()


    if value.isdigit():
        continue
    if value.isalnum():
        if key in data:
            data[key] += value
        else:
            data[key] = value


data_baru = {}
for key, value in data.items():
    if value not in data_baru:
        data_baru[value] = 1
    else:
        data_baru[value] += 1

print(data_baru)
