def rekursi(n):
    if n == 0:
        return

    rekursi(n - 1)
    print(n)

rekursi(5)
