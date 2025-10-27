a = int(input())
b = int(input())
c = int(input())

x1 = -(b+(((b**2) - (4*a*c))**0.5))/(2*a)
x2 = -(b-(((b**2) - (4*a*c))**0.5))/(2*a)

if not x2:
    x2 = 0.00
print(f'{x2:.2f}')
print(f'{x1:.2f}')
