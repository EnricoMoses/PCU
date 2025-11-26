from collections import Counter
import string

def only_letter(s):
    return [ch for ch in s.lower() if 'a' <= ch <= 'z']

def sort_key(s):
    huruf_ulang = s.split(':')[1]
    length = len(huruf_ulang)
    return -length,s

def mix(s1, s2):
    freq1 = Counter(only_letter(s1))
    freq2 = Counter(only_letter(s2))

    # print(freq1)
    # print(freq2)

    parts = []

    for ch in string.ascii_lowercase:
        f1 = freq1.get(ch, 0)
        f2 = freq2.get(ch, 0)
        max_f = max(f1, f2)

        if max_f <= 1:
            continue

        if f1 > f2:
            prefix = '1:'
        elif f2 > f1:
            prefix = '2:'
        else:
            prefix = '=:'

        parts.append(prefix + ch * max_f)

    parts.sort(key=sort_key)

    return '/'.join(parts)

s1 = input('s1 = ')
s2 = input('s2 = ')

print(mix(s1, s2))



