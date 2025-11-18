target = int(input())
n = int(input())

data = {}

for _ in range(n):
    key = input()
    value = int(input())
    data[key] = value

count = 0
for key, value in data.items():
    if target == value:
        count += 1

# if count:
#     print(count)
# else:
#     print('Angka yang dicari tidak ditemukan')

print(count) if count else print('Angka yang dicari tidak ditemukan')
