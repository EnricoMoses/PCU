m1 = [[i for i in range(3)] for j in range(2)]
m2 = [[i for i in range(3, 5)] for j in range(3)]
m3 = [[0  for i in range(len(m2[0]))]for j in range(len(m1))]

for m in range(len(m1)):
    for n in range(len(m2[0])):
        for k in range(len(m2)):
            m3[m][n] += m1[m][k] * m2[k][n]


print(m3)