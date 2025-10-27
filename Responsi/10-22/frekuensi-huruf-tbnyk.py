# butuh method counter dari libary collections untuk menghitung secara langsung jumlah kata dalam setiap kalimat
from collections import Counter

# Function Frekuensi Huruf terbanyak

# mengabaikan spasi dan perbedaan huruf-besar/kecil
# membutuhkan parameter string yang berisi kalimat
# Jika ada lebih dari satu huruf dengan frekuensi tertinggi, kembalikan yang secara alfabet lebih kecil.
# me return huruf dengan frekuensi terbanyak
def most_frequent_char(s):
    # ubah semua string ke hhuruf kecil
    s_low = s.lower()

    # saring hanya huruf (abaikan spasi dan karakter non-huruf
    letters_only = [ch for ch in s_low if ch.isalpha()]

    # jika tidak ada huruf sama sekali kembalikan string kosong
    if not letters_only:
        return ''

    # Hitung frekuensi huruf
    # fn counter akan mereturn dict dengan key: char, value: jml_char
    freq = Counter(letters_only)

    # ambil nilai frekuensi maksimum dari max value di freq
    max_freq = max(freq.values())

    # kumpulkan semua huruf yang memiliki frekuensi maksimum
    candidats = [ch for ch, f in freq.items() if f == max_freq]

    # return huruf dgn alfabet paling kecil di antara kandidat (mis: a > b)
    return min(candidats)

# Test Function
print(most_frequent_char("Hello World"))     # Output: "l"
# return a karena a paling kecil scr alfabet drpd yg lain
print(most_frequent_char("Data Science"))    # Output: "a"
print(most_frequent_char("AAaaBBbb"))        # Output: "a"




