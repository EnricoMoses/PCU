def Fahrenheit():
    return 1.8*C+32
def Kelvin():
    return C+273
def Reamur(suhu):
    return C * 0.8

C = float(input())

print(Fahrenheit())
print(Kelvin())
print(Reamur(C))