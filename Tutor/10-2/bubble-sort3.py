angka = [1,2,3,4,5,6,7,8,9]

for i in range(len(angka)):
    swapped = False
    for j in range(len(angka)-i-1):
        if angka[j] < angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
            swapped = True

        if not swapped:
            break

print(angka)

print(*angka)