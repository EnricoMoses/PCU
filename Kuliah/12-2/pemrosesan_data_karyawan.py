# Data mentah
data_mentah = "ID1001-Budi Santoso,JUNIOR,2500000;id1002-Ani Permata,SENIOR,4000000;ID1003-CITRA DEWI,INTERN,1500000"

# 1. Ekstraksi: ambil data karyawan kedua (pakai split dua kali)
entri_karyawan = data_mentah.split(";")         # split pertama → pisah per karyawan
data_karyawan2 = entri_karyawan[1]              # entri kedua (index 1)

bagian_data = data_karyawan2.split(",")         # split kedua → [ID-Nama, Posisi, Gaji]
id_nama_raw = bagian_data[0]                    # "id1002-Ani Permata"
posisi_raw = bagian_data[1]                     # "SENIOR"
gaji_raw = bagian_data[2]                       # "4000000"

# 2. Pembersihan ID: cek startswith("ID"), kalau False ubah ke huruf besar
if not id_nama_raw.startswith("ID"):
    id_nama_raw = id_nama_raw.upper()           # jadi "ID1002-ANI PERMATA"

# 3. Normalisasi Nama: pisahkan ID dan Nama, lalu ubah ke Title Case
id_part, nama_raw = id_nama_raw.split("-")      # ["ID1002", "ANI PERMATA"]
nama_rapi = nama_raw.title()                    # "Ani Permata"

# 4. Validasi posisi: cek apakah hanya huruf
posisi_valid = posisi_raw.isalpha()             # True jika hanya huruf

# 5. Format Gaji
#    - hapus semua nol di belakang (pakai rstrip('0'))
gaji_tanpa_nol_akhir = gaji_raw.rstrip("0")
if gaji_tanpa_nol_akhir == "":
    gaji_tanpa_nol_akhir = "0"

#    - format rupiah dengan pemisah ribuan titik (pakai f-string + replace)
gaji_int = int(gaji_raw)
gaji_rupiah = f"Rp{gaji_int:,.0f}".replace(",", ".")   # "Rp4.000.000"

# Output
print("=== Data Karyawan Kedua ===")
print("ID       :", id_part)
print("Nama     :", nama_rapi)
print("Posisi   :", posisi_raw)
print("Posisi hanya huruf? :", posisi_valid)
print("Gaji asli           :", gaji_raw)
print("Gaji tanpa nol akhir:", gaji_tanpa_nol_akhir)
print("Gaji format rupiah  :", gaji_rupiah)
