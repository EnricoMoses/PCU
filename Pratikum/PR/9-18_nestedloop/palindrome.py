bagian = input().split()
if len(bagian) == 2:
    L = int(bagian[0])
    H = int(bagian[1])

jumlah = 0
n = L
while n <= H:
    s = str(n)

    palin = True
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            palin = False
            break
        i += 1
        j -= 1

    if palin:
        valid = True
        k = 0
        while k < len(s):
            ch = s[k]
            if ch == '0':
                valid = False
                break
            d = ord(ch) - ord('0')
            if n % d != 0:
                valid = False
                break
            k += 1

        if valid:
            jumlah += 1

    n += 1

print(jumlah)