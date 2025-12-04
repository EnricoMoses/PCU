def analisis_nilai(data_str):
    if not isinstance(data_str, str):
        raise ValueError('Input harus berupa string')

    elemen_list = data_str.split(',')

    nilai_mahasiswa = {}

    for elemen in elemen_list:
        elemen = elemen.strip()

        if elemen == '':
            continue

        if ':' not in elemen:
            continue

        bagian = elemen.split(':')

        if len(bagian) != 2:
            continue

        nama = bagian[0].strip()
        nilai_str = bagian[1].strip()

        try:
            nilai = int(nilai_str)
        except ValueError:
            continue

        nilai_mahasiswa[nama] = nilai

    if len(nilai_mahasiswa) == 0:
        return {
            'jumlah_valid': 0,
            'rata_rata': 0,
            'tertinggi': (None, None),
            'terendah': (None, None)
        }

    jumlah_valid = len(nilai_mahasiswa)
    total_nilai = 0

    nama_tertinggi = None
    nilai_tertinggi = -99999

    nama_terendah = None
    nilai_terendah = 99999

    for nama, nilai in nilai_mahasiswa.items():
        total_nilai += nilai

        if nilai > nilai_tertinggi:
            nilai_tertinggi = nilai
            nama_tertinggi = nama

        if nilai < nilai_terendah:
            nilai_terendah = nilai
            nama_terendah = nama

    rata_rata = total_nilai / jumlah_valid

    return {
        'jumlah_valid': jumlah_valid,
        'rata_rata': rata_rata,
        'tertinggi': (nama_tertinggi, nilai_tertinggi),
        'terendah': (nama_terendah, nilai_terendah)
    }

data = "Ezra:90,Budi:100,Dewi:85,Eko:abc,Santi:95,,Fajar:88"

try:
    hasil = analisis_nilai(data)
except Exception as e:
    print(e)
    hasil ={}

print(hasil)

