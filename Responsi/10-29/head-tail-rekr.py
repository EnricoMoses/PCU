def tambah_head(n):
    if n == 0:
        return

    tambah_head(n-1)
    print(n)

def tambah_tail(n):
    if n == 0:
        return

    print(n)
    tambah_tail(n-1)


tambah_head(3)
tambah_tail(3)
