n = int(input())

data = {}
for _ in range(n):
    key = input()
    value = int(input())

    if key not in data:
        data[key] = value
    else:
        data[key] += value

for k, v in data.items():
    print(f'{k} : {v}')
