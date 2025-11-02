def persegi():
    return sisi * sisi
def lingkaran():
    return 3.14 * (sisi**2)
def segitiga():
    return (1/4)*(3**(1/2))*(sisi**2)

sisi = float(input())

print(f'{persegi():.2f}')
print(f'{lingkaran():.2f}')
print(f'{segitiga():.2f}')