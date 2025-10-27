input1, input2 = map(int, input().split())

count = 0
for i in range(input1, input2 + 1):
    temp = str(i)
    palin = True
    for j in range((1//2)*len(temp)):
        if temp[j] == temp[len(temp)-(j+1)]:
            continue
        else:
            palin = False
    if not palin:
        continue
    if temp.count('0') != 0:
        palin = False
    if not palin:
        continue

    for i in temp:
        if int(temp) % int(i) == 0:
            continue
        else:
            palin = False
            break

    if palin:
        count += 1

print(count)

