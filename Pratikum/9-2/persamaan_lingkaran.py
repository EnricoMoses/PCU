a = int(input('a = '))
b = int(input('b = '))
r = int(input('r = '))
x = int(input('x = '))
y = int(input('y = '))

persamaan = (x - a)**2 + (y - b)**2

if persamaan < r**2:
    print('titik berada di dalam lingkaran')
elif persamaan > r**2:
    print('titik berada di luar lingkaran')
elif persamaan == r**2:
    print('titik berada tepat di lingkaran')
else :
    print('Error')