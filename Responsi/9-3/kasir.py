total_belanja = int(input('Total = '))
member = input('Member(True/False) = ') == 'True'


if member and total_belanja >= 500_000:
    diskon = 0.2
elif member and total_belanja >= 200_000:
    diskon = 0.1
elif (not member) and total_belanja >= 500_000:
    diskon = 0.05
else:
    diskon = 0

total_diskon = total_belanja * diskon
total_belanja_setelah_diskon = total_belanja - total_diskon
print(f'Total bayar setelah diskon: {total_belanja_setelah_diskon}')