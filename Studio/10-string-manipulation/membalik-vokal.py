input_s = list(input().lower())


vokal = [c for c in input_s if c in 'auieo']
vokal.reverse()

idx = 0
for i in range(len(input_s)):
    if input_s[i] in 'auieo':
        input_s[i] = vokal[idx]
        idx += 1

print(''.join(input_s))

