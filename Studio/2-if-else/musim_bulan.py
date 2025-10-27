bulan = int(input())

match bulan:
    case x if 1 <= x <= 2 or x == 12:
        print('Musim Dingin')
    case x if 3 <= x <= 5:
        print('Musim Semi')
    case x if 6 <= x <= 8:
        print('Musim Panas')
    case x if 9 <= x <= 11:
        print('Musim Gugur')