import math

pi = math.pi
def tingkat1(diameterTerbesar, tinggi):
    global pi
    return pi * ((1/2) * diameterTerbesar)**2 * tinggi
def tingkat2(diameterTerbesar, tinggi):
    global pi
    return pi * ((1/2) * (2/3) * diameterTerbesar)**2 * tinggi
def tingkat3(diameterTerbesar, tinggi):
    global pi
    return pi * ((1/2) * (1/3) * diameterTerbesar)**2 * tinggi
def totalVolume(diameterTerbesar, tinggi):
    return tingkat1(diameterTerbesar, tinggi) + tingkat2(diameterTerbesar, tinggi) \
    + tingkat3(diameterTerbesar, tinggi)


diameter_terbesar = float(input())
tinggi = float(input())

print(f'{totalVolume(diameter_terbesar, tinggi):.2f}')