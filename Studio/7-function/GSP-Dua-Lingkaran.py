def panjangGarisSinggung(R, r, p):
    return (p**2 - (R+r)**2)**0.5

R = float(input())
r = float(input())
p = float(input())

print(f'{panjangGarisSinggung(R, r, p):.2f}')