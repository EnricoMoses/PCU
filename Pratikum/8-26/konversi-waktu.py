total_detik = int(input('Total detik: '))

jam = total_detik // 3600
menit = total_detik % 3600 // 60
detik = total_detik % 60


print(f'{jam}:{menit}:{detik}')