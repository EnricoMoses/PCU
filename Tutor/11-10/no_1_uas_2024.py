def minta_jumlah():
    while True:
        try:
            n = int(input('Jumlah kartu: '))
            if n <= 0:
                print('Mohon masukkan bilangan bulat positif.')
                continue
            return n
        except ValueError:
            print('Masukkan angka yang valid.')


def valid_kartu(token):
    token = token.upper()
    return (
        len(token) == 2 and
        token[0] in '0123456789' and
        token[1] in 'SBMK'
    )

def minta_kartu(n):
    line = input('Kartu (dipisah dengan spasi): ')
    tokens = [t.upper() for t in line.split()]
    if len(tokens) != n or any(not valid_kartu(t) for t in tokens):
        print('Mohon ulangi penginputan kartu!.')
        return minta_kartu(n)
    return tokens


def main():
    n = minta_jumlah()
