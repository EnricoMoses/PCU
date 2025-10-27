rows = int(input())

for i in range(1, rows + 1):
    print(' ' * (rows - i) + 'o' + ' ' * (2*i-3) + ('o' if i > 1 else ''))
for i in range(rows -1, 0, -1):
    print(' ' * (rows - i) + 'o' +' ' * (2*i-3) + ('o' if i > 1 else ''))
