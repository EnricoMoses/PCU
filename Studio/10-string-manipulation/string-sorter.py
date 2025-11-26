input_s = input().lower()

hasil = []
for kata in input_s:
    if kata.isalpha():
        hasil.append(kata)

hasil.sort()
print(''.join(hasil))