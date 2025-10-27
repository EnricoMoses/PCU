import re

N = int(input().strip())

bahan_dipakai = []
total_skor = 0

for i in range(1, N + 1):
    s = input().strip()

    if not (4 <= len(s) <= 10):
        continue

    if i == N:
        ok = bool(re.fullmatch(r"[A-Za-z0-9]+", s))
    elif i == 1:
        ok = bool(re.fullmatch(r"[A-Za-z]+", s))
    elif i % 2 == 1:
        ok = bool(re.fullmatch(r"[A-Za-z]+(\d{1,2})?", s))
    else:
        ok = bool(re.fullmatch(r"\d+", s))

    if not ok:
        continue

    bahan_dipakai.append(s)

    for ch in s:
        total_skor += ord(ch)

if total_skor < 1234:
    hasil = "Parfum Gagal"
else:
    t = str(total_skor)

    if t == t[::-1]:
        hasil = "Parfum Sempurna"
    else:
        ada_triplet = False
        for k in range(len(t) - 2):
            if t[k] == t[k+1] == t[k+2]:
                ada_triplet = True
                break

        if ada_triplet:
            hasil = "Parfum Epic"
        else:
            ada_kembar = False
            for k in range(len(t) - 1):
                if t[k] == t[k+1]:
                    ada_kembar = True
                    break

            if ada_kembar:
                hasil = "Parfum Rare"
            else:
                if total_skor % 2 == 0:
                    hasil = "Parfum Uncommon"
                else:
                    hasil = "Parfum Common"

print(hasil)
print(bahan_dipakai)
