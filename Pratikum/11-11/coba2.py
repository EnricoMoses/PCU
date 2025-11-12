# ====== FUNGSI CEK PANGRAM ======
def is_pangram(s):
    """
    Mengembalikan True jika s mengandung semua huruf a-z minimal sekali.
    Hanya huruf a-z yang dihitung; case-insensitive.
    Tidak memakai set: gunakan dictionary sebagai penanda.
    """
    seen = {}  # key: huruf a-z, value: True (atau hitungan)
    for ch in s:
        c = ch.lower()
        if 'a' <= c <= 'z':      # hanya alfabet latin
            # tandai huruf sudah muncul
            # (boleh pakai 1 sebagai penanda; yang penting kuncinya ada)
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
            # optimalisasi kecil: kalau sudah 26 huruf, boleh berhenti
            if len(seen) == 26:
                return True
    return len(seen) == 26


# ====== FUNGSI CEK ISOMORFIK ======
def is_isomorphic(s1, s2):
    """
    Mengembalikan True jika s1 dan s2 isomorfik:
    - Ada pemetaan 1-1 dari tiap karakter di s1 ke karakter di s2.
    - Konsisten di seluruh posisi.
    - Panjang harus sama (karakter termasuk spasi).
    Tidak memakai zip/set: loop by index, pakai dua dictionary.
    """
    if len(s1) != len(s2):
        return False

    map12 = {}  # pemetaan dari char s1 -> char s2
    map21 = {}  # pemetaan balik dari char s2 -> char s1 (untuk jaga bijektif)

    i = 0
    n = len(s1)
    while i < n:
        a = s1[i]
        b = s2[i]

        # jika sudah ada pemetaan a->?, harus konsisten == b
        if a in map12:
            if map12[a] != b:
                return False
        else:
            # a belum dipetakan: pastikan b juga belum dipetakan dari char lain
            if b in map21 and map21[b] != a:
                return False
            # tetapkan pemetaan dua arah
            map12[a] = b
            map21[b] = a
        i += 1

    return True


# ====== PROGRAM UTAMA ======
def main():
    # Baca dua baris input (masing-masing satu string)
    s1 = input().rstrip("\n")
    s2 = input().rstrip("\n")

    pangram_ok = is_pangram(s1) or is_pangram(s2)
    iso_ok = is_isomorphic(s1, s2)

    # Aturan output:
    # - Jika ada pangram (salah satu) DAN isomorfik -> "Pangram Isomorfik"
    # - Jika ada pangram saja -> "Pangram"
    # - Jika isomorfik saja -> "Isomorfik"
    # - Selain itu -> "Bukan Keduannya"
    if pangram_ok and iso_ok:
        print("Pangram Isomorfik")
    elif pangram_ok:
        print("Pangram")
    elif iso_ok:
        print("Isomorfik")
    else:
        print("Bukan Keduannya")


if __name__ == "__main__":
    main()
