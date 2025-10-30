import math

def Trigonometri(n):
    print(f'{math.sin(n):.2f}')
    print(f'{math.cos(n):.2f}')
    print(f'{math.tan(n):.2f}')

n = float(input())
n = math.radians(n)
Trigonometri(n)