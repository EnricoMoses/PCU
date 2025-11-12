def is_pangram(s):
    daftar_huruf = {}
    for char in s:
        char = char.lower()
        if 'a' <= char <= 'z':
            if char not in daftar_huruf:
                daftar_huruf[char] = 1
            else:
                daftar_huruf[char] += 1

            if len(daftar_huruf) == 26:
                return True
    return len(daftar_huruf) == 26

def is_isomorfik(s1, s2):
    if len(s1) != len(s2):
        return False

    dic_a = {}
    dic_b = {}

    i = 0
    n = len(s1)
    while i < n:
        a = s1[i]
        b = s2[i]

        if a in dic_a:
            if dic_a[a] != b:
                return False
        else:
            if b in dic_b and dic_b[b] != a:
                return False

            dic_a[a] = b
            dic_b[b] = a
        i += 1
    return True

s1 = input()
s2 = input()

pangram_1 = is_pangram(s1)
pangram_2 = is_pangram(s2)
isomorfik = is_isomorfik(s1, s2)

if (pangram_1 or pangram_2) and isomorfik:
    print('Pangram isomorfik')
elif pangram_1 or pangram_2:
    print('Pangram')
elif isomorfik:
    print('Isomorfik')
else:
    print('Bukan Keduanya')