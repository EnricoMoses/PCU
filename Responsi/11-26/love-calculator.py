def char_to_value(kata):
    kata = kata.upper()
    if 'A' <= kata <= 'Z':
        return ord(kata) - ord('A') + 1
    return 0

def name_to_sum(nama):
    total = 0
    for char in nama:
        total += char_to_value(char)
    return total

def reduce_to_one_digit(n):
    while n >= 10:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n

def compatibility_percentage(d1, d2):
    small = min(d1, d2)
    big = max(d1, d2)
    return small / big * 100

nama1= input('Nama 1 : ')
nama2= input('Nama 2 : ')

sum1 = name_to_sum(nama1)
sum2 = name_to_sum(nama2)

digit1 = reduce_to_one_digit(sum1)
digit2 = reduce_to_one_digit(sum2)

percent = compatibility_percentage(digit1, digit2)

print(f'Nilai akhir {nama1} = {digit1}')
print(f'Nilai akhir {nama2} = {digit2}')
print(f'Tingkat kecocokan: {percent:.2f}%')

