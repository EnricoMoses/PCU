string_asli = "Halo dunia😊"
byte_utf8 = string_asli.encode('utf-8')
print((byte_utf8))

print("key=values".partition("="))

print('baaaaaniania'.find('na'))

print('ha ha ha ha ha'.replace(' ', ''))

def balik_string(s):
    return s[::-1]

print(balik_string('abcd'))

def jml_vokal(s):
    total = 0
    for char in s:
        if char in 'aiueo':
            total += 1

    return total

print(jml_vokal('abcdefg'))

print('michael ganteng'.title())

def is_palindrome(s):
    clear = s.replace(' ', '')
    return clear == balik_string(clear)

print(is_palindrome('abcd'))
print(is_palindrome('su gus'))


