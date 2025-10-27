# KPK & FPB dari faktorisasi (tanpa function, tanpa dict)

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Faktorisasi a → faktor_a (list)
x = a
i = 2
faktor_a = []
while x > 1:
    if x % i == 0:
        faktor_a.append(i)
        x //= i
    else:
        i += 1

# Faktorisasi b → faktor_b (list)
y = b
i = 2
faktor_b = []
while y > 1:
    if y % i == 0:
        faktor_b.append(i)
        y //= i
    else:
        i += 1

print("\nFaktorisasi", a, ":", " x ".join(str(k) for k in faktor_a))
print("Faktorisasi", b, ":", " x ".join(str(k) for k in faktor_b))

# FPB = perkalian faktor yang sama (dengan memperhatikan banyaknya)
fpb = 1
sisa_b = faktor_b[:]          # salin supaya faktor_b asli tidak berubah
for f in faktor_a:
    if f in sisa_b:
        fpb *= f
        sisa_b.remove(f)      # buang satu kopi faktor yang dipakai

# KPK = semua faktor a dikali sisa faktor b (yang belum dipakai FPB)
kpk = 1
for f in faktor_a:            # ini sama dengan nilai a
    kpk *= f
for f in sisa_b:              # ini menambah faktor dari b yang belum ada di a
    kpk *= f

print("\nFPB =", fpb)
print("KPK =", kpk)
