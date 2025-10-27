def hitung_nilai(lst):
    # Kasus 1, cari total
    total = 0
    for i in lst:
        total += i

    # Kasus 2, cari median
    sorted_list = sorted(lst)
    n = len(sorted_list)

    if n % 2 == 1:  # list dengan panjang ganjil
        median = sorted_list[n // 2]
    else:  # list dengan panjang genap
        middle_1 = sorted_list[n // 2 - 1]
        middle_2 = sorted_list[n // 2]
        median = (middle_1 + middle_2) / 2

    # kasus 3 cari rata-rata
    rata = total / len(lst)


    return [rata, total, median]

print(hitung_nilai([1,2,3,4,5,6,7,8]))
