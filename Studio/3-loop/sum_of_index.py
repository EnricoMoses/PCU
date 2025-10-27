angka = int(input())
target = int(input())

angka = str(angka)

curr = 0
sum_index = 0
found = False

for i, char in enumerate(angka):
    digit = int(char)
    # hanya tambahkan jika tidak melebihi target
    if curr + digit <= target:
        curr += digit
        sum_index += i
        if curr == target:
            found = True
            break

print(sum_index if found else -1)