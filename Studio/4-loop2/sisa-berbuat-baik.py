# Baca n
n = int(input())

# Baca pasangan pertama (a, b)
ab = input().split()
a = int(ab[0]); b = int(ab[1])

# x harus ≡ b (mod a) untuk kloter pertama
x = b
step = a  # langkah awal

# Proses kloter berikutnya
for _ in range(n - 1):
    ab = input().split()
    a = int(ab[0]); b = int(ab[1])

    # Naikkan x per 'step' sampai cocok sisa bagi terhadap a
    while x % a != b:
        x += step

    # Hitung gcd(step, a) dengan loop Euclid (tanpa fungsi)
    p = step
    q = a
    while q != 0:
        t = p % q
        p = q
        q = t
    g = p  # gcd

    # step = KPK(step, a) = step // gcd * a
    step = (step // g) * a

# Cetak x terkecil yang memenuhi semua kloter
print(x)
