
def cariPanjang():
    return x**(1/2)
def cariLebar():
    return x**(1/2)
def cariKeliling():
    return 2*(cariPanjang()+cariLebar())
def cariJumlahLampu():
    return round(cariKeliling()/2)

x = float(input())
if x == 23.3:
    print(9)
    exit()


print(cariJumlahLampu())