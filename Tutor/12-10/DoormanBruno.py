X = int(input())
queue = list(input().strip())

women = men = 0
count = 0

while queue:
    newM1 = newM2 = men
    newW1 = newW2 = women

    if queue[0] == 'W':
        newW1 += 1
    else:
        newM1 += 1

    if len(queue) > 1:
        if queue[1] == 'W':
            newW2 += 1
        else:
            newM2 += 1
    else:
        newW2 = newM2 = None

    if abs(newM1 - newW1) <= X:
        men, women = newM1, newW1
        queue.pop(0)
    elif newW2 is not None and newM2 is not None and abs(newM2 - newW2) <= X:
        men, women = newM2, newW2
        queue.pop(1)
    else:
        break

    count += 1

print(count)
