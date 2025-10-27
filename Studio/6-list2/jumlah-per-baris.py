inp1 = input().split()
baris = int(inp1[0])
kolom = int(inp1[1])
# print(inp1)
list2d = []
for i in range(baris):
    temp = []
    inp3 = input().split()
    for j in range(kolom):
        temp.append(int(inp3[j]))
    list2d.append(temp)

for i in range(len(list2d)):
    total = 0
    for j in range(len(list2d[0])):
        total += list2d[i][j]
    print(total)
