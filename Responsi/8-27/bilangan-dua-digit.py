bilangan = int(input("Masukkan bilangan dua digit: "))

puluhan = bilangan // 10
satuan = bilangan % 10
# if puluhan < satuan:
#     selisih = satuan - puluhan
# else :
#     selisih = puluhan - satuan

print('=== HASIL PERHITUNGAN ===')
print(f'Bilangan : {bilangan}')
print(f'Puluhan  : {puluhan}')
print(f'Satuan   : {satuan}')
print(f'Selisih  = {abs(puluhan - satuan)}')