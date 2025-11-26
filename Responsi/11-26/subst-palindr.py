def is_palindrome(s):
    return s == s[::-1]

def palindrome_terpanjang(s):
    n = len(s)
    terpanjang = s[0]

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if is_palindrome(sub) and len(sub) > len(terpanjang):
                terpanjang = sub

    return terpanjang
text = input('Masukkan sebuah string: ')
result = palindrome_terpanjang(text)
print(result)