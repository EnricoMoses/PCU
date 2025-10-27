berat_badan_awal = float(input("Berat badan Awal : "))
berat_badan_tujuan = float(input("Berat badan tujuan : "))
durasi_hari = int(input("Durasi: "))

selisih_berat = berat_badan_awal - berat_badan_tujuan
total_kalori_yang_dibakar = 7000 * selisih_berat
jarak_tempuh = total_kalori_yang_dibakar / 80
jarak_harian = jarak_tempuh / durasi_hari

print(f'Kalori yang harus dibakar: {int(total_kalori_yang_dibakar)} kalori')
print(f'Total Jarak yang harus ditempuh: {jarak_tempuh:.2f} Km')
print(f'Jarak yang harus ditempuh setiap hari = {int(jarak_tempuh)} / {durasi_hari} = {jarak_harian:.2f} Km')