from collections import Counter
import string

def only_letters(s: str):
    """Ambil hanya huruf a-z dan ubah ke lowercase."""
    return [ch for ch in s.lower() if 'a' <= ch <= 'z']

def build_freq(s: str):
    """Bangun Counter frekuensi huruf dari sebuah string."""
    return Counter(only_letters(s))

def sort_key(seg: str):
    """
    Fungsi key untuk sorting:
    - Utama: panjang bagian huruf (descending → pakai minus)
    - Kedua: urutan alfabetis berdasarkan seluruh substring
    """
    # seg bentuknya seperti "1:aaaaa" atau "=:bb"
    huruf_ulang = seg.split(":")[1]
    length = len(huruf_ulang)
    return (-length, seg)

def mix(s1: str, s2: str) -> str:
    freq1 = build_freq(s1)
    freq2 = build_freq(s2)

    parts = []

    for ch in string.ascii_lowercase:
        f1 = freq1.get(ch, 0)
        f2 = freq2.get(ch, 0)
        max_f = max(f1, f2)

        # hanya jika frekuensi maksimum > 1
        if max_f <= 1:
            continue

        # tentukan prefix
        if f1 > f2:
            prefix = "1:"
        elif f2 > f1:
            prefix = "2:"
        else:
            prefix = "=:"

        parts.append(prefix + ch * max_f)

    # PAKAI FUNGSI sort_key, bukan lambda
    parts.sort(key=sort_key)

    return "/".join(parts)


# ====== Contoh pemakaian ======
s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
print(mix(s1, s2))   # 1:aaaaa/2:bbb

s1 = "Xxxyyyyz"
s2 = "Xxyyzz"
print(mix(s1, s2))   # 1:yyyy/1:xxx/2:zz

s1 = "bbcc"
s2 = "bccb"
print(mix(s1, s2))   # =:bb/=:cc