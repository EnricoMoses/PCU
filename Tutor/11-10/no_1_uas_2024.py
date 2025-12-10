urutan_angka = {str(i): i-1 for i in range(1, 10)}
urutan_angka['0'] = 9

urutan_simbol = {'K': 0, 'M':1, 'B':2, 'S':3}

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
        print('Mohon ulangi penginputan kartu!')
        return minta_kartu(n)
    return tokens

def to_tuple_list(tokens):
    return [(t[0], t[1], t) for t in tokens]

def card_sorting(cards_tuples, hasil):
    if len(cards_tuples) == 0:
        return hasil

    highest = cards_tuples[0]

    for r, s, kode in cards_tuples[1:]:
        if urutan_angka[r] > urutan_angka[highest[0]]:
            highest = (r, s, kode)
        elif urutan_angka[r] == urutan_angka[highest[0]]:
            if urutan_simbol[s] > urutan_simbol[highest[1]]:
                highest = (r, s, kode)


    idx = cards_tuples.index(highest)
    cards_tuples.pop(idx)
    hasil.append(highest[2])

    return card_sorting(cards_tuples, hasil)

def main():
    n = minta_jumlah()
    tokens = minta_kartu(n)
    cards_tuples = to_tuple_list(tokens)
    hasil = card_sorting(cards_tuples, [])
    print('Hasil pengurutan:', ' '.join(hasil))


main()
