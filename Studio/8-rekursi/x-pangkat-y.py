a = int(input())
b = int(input())

def power(x, y):
    if y == 0:
        return 1
    if y < 0:
        return 0
    return x * power(x, y-1)

def factors_str(x, y):
    if y == 1:
        return str(x)
    return str(x) + 'x' + factors_str(x, y-1)

hasil = power(a, b)
deret = factors_str(a, b)

print(f'{a}^{b}={deret}={hasil}')
