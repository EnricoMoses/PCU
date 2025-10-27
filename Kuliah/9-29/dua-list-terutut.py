list1 = [1, 2, 5, 8]
list2 = [2, 4, 9]

i = j = 0
list_gabungan = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        list_gabungan.append(list1[i])
        i += 1
    else:
        list_gabungan.append(list2[j])
        j += 1

while i < len(list1):
    list_gabungan.append(list1[i])
    i += 1

while j < len(list2):
    list_gabungan.append(list2[j])
    j += 1

print(list_gabungan)