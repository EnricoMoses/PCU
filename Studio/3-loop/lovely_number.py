n = int(input())

# Cek prima
prima = True
if n < 2 :
    prima = False
else:
    for i in range(2, n):
        if n % i == 0:
            prima = False
            break

# cek apakah 3 digit
ada3 = False
for ch in str(n):
    if ch == '3':
        ada3 = True
        break

if prima and ada3 :
    print('YES')
else :
    print('NO')