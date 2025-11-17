nilai = {
    "Aaron": (85, 90, 88),
    "Ezra": (92, 89, 95),
    "XR": (78, 82, 80)
}

def avg_scores_per_student(data):
    hasil = {}
    for nama, skor_tuple in data.items():
        rata = sum(skor_tuple) / len(skor_tuple)
        hasil[nama] = rata
    return hasil

def best_student(avg_dict):
    # key=lambda kv: kv[1] arti nya bandingkan berdasarkan nilai rata rata
    return max(avg_dict.items(), key=lambda kv: kv[1])

avg1 = avg_scores_per_student(nilai)
for nama in nilai:
    print(f"{nama}: {avg1[nama]:.2f}")
terbaik_nama, terbaik_nilai = best_student(avg1)
print(f"Mahasiswa terbaik: {terbaik_nama}")