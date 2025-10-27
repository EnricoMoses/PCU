inp1 = input().split()
baris = int(inp1[0])
kolom = int(inp1[1])
inp2 = input()
list2d = []
for i in range(baris):
    temp = []
    inp3 = input().split()
    for j in range(kolom):
        temp.append(int(inp3[j]))
    list2d.append(temp)

x = int(inp2)
# for i in range(0, baris, x):
#     baris_baru = []
#     for j in range(0, kolom, x):
#         baris_baru.append(str(list2d[i][j]))
#     print(' '.join(baris_baru))

list_baru = []
for i in range(0, baris, x):
    baris_baru = []
    for j in range(0, kolom, x):
        baris_baru.append(list2d[i][j])
    list_baru.append(baris_baru)

for i in range(len(list_baru)):
    for j in range(len(list_baru[0])):
        print(list_baru[i][j], end=' ')
    print()

