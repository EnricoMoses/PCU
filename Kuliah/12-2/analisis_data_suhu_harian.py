import numpy as np
import matplotlib.pyplot as plt

hari = np.array([1, 2, 3, 4, 5, 6, 7])

suhu_A = np.array([28, 30, 29, 31, 32, 30, 29])  # Kota A
suhu_B = np.array([26, 28, 30, 32, 34, 31, 29])  # Kota B

mean_A = np.mean(suhu_A)
mean_B = np.mean(suhu_B)

selisih_harian = suhu_A - suhu_B
maks_selisih = np.max(np.abs(selisih_harian))

print("Rata-rata suhu Kota A:", mean_A)
print("Rata-rata suhu Kota B:", mean_B)
print("Selisih harian (A - B):", selisih_harian)
print("Selisih maksimum |A - B|:", maks_selisih)

m, c = np.polyfit(hari, suhu_B, 1)

hari_8 = 8
pred_hari_8 = m * hari_8 + c
print(f"Perkiraan suhu Kota B pada hari ke-8: {pred_hari_8:.2f} °C")

plt.figure(figsize=(8, 5))

# Garis suhu Kota A dan Kota B
plt.plot(hari, suhu_A, marker='o', label='Kota A')
plt.plot(hari, suhu_B, marker='s', label='Kota B')

# Garis tren linear untuk Kota B
hari_tren = np.array([1, 8])               # dari hari ke-1 sampai ke-8
suhu_tren_B = m * hari_tren + c
plt.plot(hari_tren, suhu_tren_B, linestyle='--', label='Tren Kota B')

# Prediksi titik hari ke-8 untuk Kota B
plt.scatter(hari_8, pred_hari_8, marker='x', s=80, label='Prediksi Hari ke-8 (Kota B)')

# Pengaturan grafik
plt.title('Perbandingan Suhu Harian Kota A dan Kota B')
plt.xlabel('Hari')
plt.ylabel('Suhu Maksimum (°C)')
plt.xticks(hari)  # sumbu x dari 1 sampai 7
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()