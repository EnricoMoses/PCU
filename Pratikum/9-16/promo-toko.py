a = int(input('a = '))
b = int(input('b = '))
x = int(input('c = '))

kupon = a + b
tambahan = 0

while kupon >= x:
    tukar = kupon // x
    tambahan += tukar

    kupon = (kupon % x) + tukar

print(tambahan)