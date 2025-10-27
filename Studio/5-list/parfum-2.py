N = int(input().strip())

bahan_dipakai = []
total_skor = 0

for i in range(1, N + 1):
    s = input().strip()

    if not (4 <= len(s) <= 10):
        continue

    ok = False

    if i == N:
        ok = s.isalnum()

    elif i == 1:
        ok = s.isalpha()

    elif i % 2 == 1:
        j = 0
        while j < len(s) and s[j].isalpha():
            j += 1
        prefix_huruf = (j > 0) and all(ch.isalpha() for ch in s[:j])
        suffix = s[j:]
        ok = prefix_huruf and (len(suffix) in (0, 1, 2)) and all(ch.isdigit() for ch in suffix)

    else:
        ok = s.isdigit()

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
                hasil = "Parfum Uncommon" if total_skor % 2 == 0 else "Parfum Common"

print(hasil)
print(bahan_dipakai)
