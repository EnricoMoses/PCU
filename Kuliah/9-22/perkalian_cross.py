m_1 = [[1,2], [2, 3]]
m_2 = [[4, 5], [6, 7]]

m_3 = [[0,0], [0, 0]]

for i in range(2):
    for j in range(2):
        total = 0
        for k in range(2):
            total += m_1[i][k] * m_2[k][j]
        m_3[i][j] = total

print(m_3)