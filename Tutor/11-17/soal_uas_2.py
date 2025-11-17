from itertools import combinations

layanan = [
    ["Adi", 1.5, 12],
    ["Budi", 1, 10],
    ["C", 3, 30],
    ["D", 5.5, 30],
    ["E", 4, 15],
    ["F", 4.5, 20],
    ["G", 3.5, 10],
]

maks_duration = 7

min_biaya = 1000000
hasil = []

for i in range(1, len(layanan)):
    for comb in combinations(layanan, i):
        # total_jam = 0
        # total_biaya = 0
        # for x in comb:
        #     total_jam += x[1]
        #     total_jam += x[2]
        total_jam = sum(x[1] for x in comb)
        total_biaya = sum(x[2] for x in comb)
        if total_jam <= 7 :
            if i > len(hasil):
                hasil = comb
                min_biaya = total_biaya
            elif i == len(hasil) and min_biaya > total_biaya:
                hasil = comb
                min_biaya = total_biaya

print(hasil)