class SaldoError(Exception):
    pass
saldo = 50000
try:
    tarik = int(input("Masukkan jumlah penarikan: "))
    if tarik > saldo:
        raise SaldoError("Saldo tidak cukup")
    saldo -= tarik
    print("Penarikan berhasil. Saldo sekarang:", saldo)
except ValueError:
    print("Input harus berupa angka!")
except SaldoError as e:
    print("Error:", e)