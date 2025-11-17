nilai_mahasiswa = {
    "Aaron": {
        "Algoritma": (85, 90, 82),
        "Basis Data": (78, 80, 85)
    },
    "Ezra": {
        "Algoritma": (92, 95, 90),
        "Basis Data": (88, 84, 86)
    },
    "XR": {
        "Algoritma": (70, 75, 72),
        "Basis Data": (80, 82, 78)
    }
}

def avg_per_student_per_subject(data):
    hasil = {}
    for nama, matkul_map in data.items():
        hasil[nama] = {}
        for matkul, skor_tuple in matkul_map.items():
            hasil[nama][matkul] = sum(skor_tuple) / len(skor_tuple)
    return hasil

def class_avg_per_subject(data):
    sum_per_matkul = {}
    cnt_per_matkul = {}
    for _, matkul_map in data.items():
        for matkul, skor_tuple in matkul_map.items():
            if matkul not in sum_per_matkul:
                sum_per_matkul[matkul] = 0
                cnt_per_matkul[matkul] = 0
            sum_per_matkul[matkul] += sum(skor_tuple)
            cnt_per_matkul[matkul] += len(skor_tuple)
    return {m: sum_per_matkul[m] / cnt_per_matkul[m] for m in cnt_per_matkul}


avg_mhs = avg_per_student_per_subject(nilai_mahasiswa)
avg_kelas = class_avg_per_subject(nilai_mahasiswa)

print("=== Rata-rata per Mahasiswa ===")
for nama in ["Aaron", "Ezra", "XR"]:
    alg = avg_mhs[nama]["Algoritma"]
    bd  = avg_mhs[nama]["Basis Data"]
    print(f"{nama}: Algoritma={alg:.2f}, Basis Data={bd:.2f}")

print("=== Rata-rata Kelas ===")
print(f"Algoritma: {avg_kelas['Algoritma']:.2f}")
print(f"Basis Data: {avg_kelas['Basis Data']:.2f}")


