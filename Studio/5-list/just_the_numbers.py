n = input()

total = 0
for i in n:
    if '0' <= i <= '9':
        total += int(i)
        i = total

print(total)