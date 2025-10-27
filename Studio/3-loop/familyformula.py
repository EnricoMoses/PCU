temp = int(input())
total = temp
while True:
    a = input()
    if a == 'END':
        break
    total = temp + int(a)
    temp = total

    b = input()
    if b == 'END':
        break
    total = temp - int(b)
    temp = total

print(total)