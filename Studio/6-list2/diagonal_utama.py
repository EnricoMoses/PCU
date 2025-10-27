inp1 = input().split()
baris = int(inp1[0])
kolom = int(inp1[1])
list2d = []
for i in range(baris):
    temp = []
    inp3 = input().split()
    for j in range(kolom):
        temp.append(int(inp3[j]))
    list2d.append(temp)

# print(list2d)
# for i in range(len(list2d)):
#     idx_tengah = 0
#     for j in range(len(list2d[0])):
#         idx_tengah = j // len(list2d[0]) + 1
#     print(list2d[i][idx_tengah])

for i in range(len(list2d)):
    # idx_diagonal = 0
    # for j in range(len(list2d[0])):
    # print(i)
    # print(i)
    print(list2d[i][i], end=' ')