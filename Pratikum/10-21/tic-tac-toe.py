def make_board(n):
    # buat papan n x n
    return [['.' for _ in range(n)] for _ in range(n)]

def print_board(board):
    # print papan
    for row in board:
        print(' '.join(row))

def is_valid_move(board, r, c):
    # true jika kordinat valid dan sel masih kosong
    n = len(board)
    return 0 <= r <= n and 0 <= c <= n and board[r][c] == '.'

def check_win(board, player):
    # check apakah player menang
    n = len(board)

    # baris
    for r in range(n):
        if all(board[r][c] == player for c in range(n)):
            return True

    # kolom
    for c in range(n):
        if all(board[r][c] == player for r in range(n)):
            return True

    # diagonal utama
    if all(board[i][i] == player for i in range(n)):
        return True

    # diagonal miring
    if all(board[i][n - 1 - i] == player for i in range(n)):
        return True

    return False

def is_full(board):
    # true jika papan penuh
    return all(cell != '.' for row in board for cell in row)

def game():

    while True:
        n = int(input('Masukkan ukuran papan: '))
        if n <= 0:
            print('Ukuran harus bilangan positif')
            continue
        break

    board = make_board(n)

    print('Papan awal:')
    print_board(board)
    print()

    current = 'X' # X jalan duluan
    while True:
        prompt = f'Giliran {current} - masukkan baris dan kolom: '
        raw = input(prompt).strip().split()
        if len(raw) != 2:
            print(f'Input tidak valid. Masukkan dua angka 0-{n-1}')
            continue

        r, c = map(int, raw)

        if not is_valid_move(board, r, c):
            print('Kotak sudah terisi atau koordinat di luar papan')
            continue

        # Lakukan gerakan
        board[r][c] = current
        print_board(board)
        print()

        # Cek menang
        if check_win(board, current):
            print(f'Pemain {current} menang!')
            break

        if is_full(board):
            print('Seri!')
            break

        # ganti pemain
        current = 'O' if current == 'X' else 'X'


game()
