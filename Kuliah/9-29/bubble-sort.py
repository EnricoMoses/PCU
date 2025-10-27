listt = [8, 10, 6, 2, 4]

swapped = True
while swapped:
    swapped = False
    for i in range(len(listt) - 1):
        if listt[i] > listt[i + 1]:
            swapped = True
            listt[i], listt[i + 1] = listt[i + 1], listt[i]


print(listt)