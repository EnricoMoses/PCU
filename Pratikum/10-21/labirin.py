def find_char(maze, target):
    # Cari posisi (row, col) dr karakter di maze
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return (r, c)
    return None

def render(maze, dono_pos, start_pos):

    for r in range(len(maze)):
        line = []
        for c in range(len(maze[0])):
            if (r, c) == dono_pos:
                line.append('D')
            elif (r, c) == start_pos and dono_pos != start_pos:
                line.append('S')
            else:
                line.append(maze[r][c])
        print(' '.join(line))
    print('-' * 20)


def next_pos(pos, move_key):
    # Hitung posisi selanjutnya dari WASD
    r, c = pos
    key = move_key.lower()
    if key == 'w':
        return (r - 1, c)
    elif key == 's':
        return (r + 1, c)
    elif key == 'a':
        return (r, c - 1)
    elif key == 'd':
        return (r, c + 1)
    return pos # jika tomboll tdk valid, return posisi semula

def valid_and_not_wall(maze, pos):
    # Cek pos dalam batas dan bukan tembok X
    r, c = pos
    rows, cols = len(maze), len(maze[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return False
    if maze[r][c] == 'X':
        return False
    return True

def is_end(maze, pos):
    # Cek apakaah pos adalah  E
    r, c = pos
    return maze[r][c] == 'E'

def game_loop(maze):
    print('=== Petualangan Ksatria Dono ===')
    print('Gunakan W/A/S/D untuk bergerak. Cari posisi E (Putri Yanti)!\n')

    start_pos = find_char(maze, 'S')
    end_pos = find_char(maze, 'E')
    if start_pos is None or end_pos is None:
        print('Maze tidak valid, S atau E tidak di temukan')
        return

    dono_pos = start_pos

    render(maze, dono_pos, start_pos)

    while True:
        move = input('Masukkan pergerakan (W/A/S/D): ')
        if move.lower() not in ('w', 'a', 's', 'd'):
            print('Input tidak valid, Gunakan (W/A/S/D)!')
            continue

        calon_pos = next_pos(dono_pos, move)

        if not valid_and_not_wall(maze, calon_pos):
            print('Tidak bisa lewat! Ada tembok atau keluar dari batas labirin.')
            render(maze, dono_pos, calon_pos)
            continue

        dono_pos = calon_pos

        render(maze, dono_pos, calon_pos)

        # cek apakah sampai ke E
        if is_end(maze, calon_pos):
            r, c = dono_pos
            print(f'Selamat! Dono menemukan Putri Yanti di posisi ({r}, {c}) ')
            break

labirin = [
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'E'],
    ['.', '.', 'X', 'X', 'X'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'S']
]
game_loop(labirin)
