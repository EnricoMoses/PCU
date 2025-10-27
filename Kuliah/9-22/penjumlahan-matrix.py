m_1 = [[1,2,3],[4,5,6],[7,8,9]]
m_2 = [[1,2,3],[4,5,6],[7,8,9]]

m_3 = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(m_1[i][j] + m_2[i][j])
    m_3.append(baris)

print(m_3)
