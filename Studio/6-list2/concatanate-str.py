# hasil = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

hasil = [[x for x in range(1, 4)] for y in range(3)]

for r in hasil:
    print(' '.join(str(v) for v in r))
    # print([str(v) for v in r])