def jumlah_kata(s):
    clear = s.split()
    return len(clear)

print(jumlah_kata('ha ha aha sldh'))

def jumlah_upper(s):
    total = 0
    for kata in s:
        if kata.isupper():
            total += 1

    return total

print(jumlah_upper("HeLLo PYthon"))  # 5

def hapus_punctuation(s):
    s_baru = []
    for kata in s:
        if kata.isalnum():
            s_baru.append(kata)
        elif kata == ' ':
            s_baru.append(kata)

    return ''.join(s_baru)

print(hapus_punctuation("Hello, world!!!"))

def hitung_karakter(s):
    dict_karakter = {}
    for kata in s:
        if kata not in dict_karakter:
            dict_karakter[kata] = 1
        else:
            dict_karakter[kata] += 1

    return dict_karakter

print(hitung_karakter("abbapaab"))


def normalisasi(s):
    s_baru = ' '.join(s.strip().split())
    return s_baru.capitalize()

print(normalisasi("   hELLO    WoRLD   "))

def balik_kata(s):
    s_list = s.strip().split()
    return ' '.join(s_list[::-1])

print(balik_kata("saya suka python"))

def kata_vokal(s):
    s_list = s.lower().split()
    total = 0
    for kata in s_list:
        for huruf in kata:
            if huruf in 'aiueo':
                total += 1
                break

    return f'{total} kata punya vokal'

print(kata_vokal("aku makan nasi goreng"))

def sensor_angka(s):
    baru = []
    for ch in s:
        if ch.isdigit():
            baru.append('X')
        else:
            baru.append(ch)

    return ''.join(baru)

print(sensor_angka("Ruangan 204 lantai 3"))

def semua_indeks(teks, sub):
    indeks = []
    start = 0

    # kalau sub kosong, kembalikan list kosong saja
    if sub == "":
        return indeks

    while True:
        pos = teks.find(sub, start)  # cari sub mulai dari posisi start
        if pos == -1:               # kalau tidak ketemu, selesai
            break
        indeks.append(pos)          # simpan posisi yang ketemu
        start = pos + 1             # geser start supaya bisa cari kemunculan berikutnya (boleh overlap)

    return indeks

print(semua_indeks("banana", "na"))

def format_nama(s):
    return s.title()

print(format_nama("Anita ROGER"))

def cek_password(pw):
    valid = False
    valid_upper = False
    valid_lower = False
    valid_number = False

    if len(pw) > 8:
        for kata in pw:
            if kata.isupper():
                valid_upper = True
            if kata.isdigit():
                valid_number = True
            if kata.islower():
                valid_lower = True

    valid = valid_upper and valid_lower and valid_number
    if valid:
        return 'valid'
    return 'tidak valid'

print(cek_password('Enricokdfs'))

def kata_unik(s):
    s_list = s.lower().split()
    s_baru = []
    for kata in s_list:
        if kata not in s_baru:
            s_baru.append(kata)

    return len(s_baru)

print(kata_unik("saya suka makan makan nasi"))


