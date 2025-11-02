def fibbonaci(n):
    el1, el2 = 1, 1
    # ts = 0
    total = 0
    for i in range(1, n+1):
        print(el1, end='')
        total += el1
        if i < n:
            print('+', end='')
        else:
            print('=', end='')
        ts = el1 + el2
        el1, el2 = el2, ts
    print(total)


fibbonaci(10)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

