def sum_nilai_nama(nama, idx= 0):
    if idx == len(nama):
        return 0

    ch = nama[idx].upper()

    if 'A' <= ch <= 'Z':
        nilai = ord(ch) - ord('A') + 1
    else:
        nilai = 0 # selain huruf kasi 0

    return nilai + sum_nilai_nama(nama, idx + 1)

def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

def satu_digit(n):
    if n < 10:
        return n
    return satu_digit(sum_digit(n))

nama1 = input('Nama1: ')
nama2 = input('Nama2: ')

total1 = sum_nilai_nama(nama1)
total2 = sum_nilai_nama(nama2)

digit1 = satu_digit(total1)
digit2 = satu_digit(total2)

if digit1 == 0 or digit2 == 0:
    persen = 0
else:
    kecil = min(digit1, digit2)
    besar = max(digit1, digit2)
    persen = (kecil/besar)*100

print(f'{persen:.2f}%')






