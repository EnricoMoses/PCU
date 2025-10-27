a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

x = a
y = b

while b != 0:
    sisa = a % b
    a = b
    b = sisa

fpb = a
kpk = (x * y) // fpb

print("FPB =", fpb)
print("KPK =", kpk)