x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if dx == 0 or dy == 0 or abs(dx) == abs(dy):
    print('Perbatasan')
else :
    if dx > 0 and dy > 0 : # kudran kanan atas
        if dx > dy :
            print('Go') # lebih ke arah timur (antara timur laut dan timur)
        elif dx < dy :
            print('Al') # lebih ke arah utara (antara utara dan timur laut)
    elif dx > 0 > dy: # dx > 0 or dy < 0 Kuadran kanan bawah
        if dx > abs(dy):
            print('Rit') # lebih ke timur (antara timur dan tenggara)
        elif abs(dy) > dx :
            print('Ma') # lebih ke selatan (antara tenggara dan selatan)
    elif dx < 0 and dy < 0: # kuadran kiri bawah
        if abs(dy) > abs(dy):
            print('Rog') # lebih ke barat (antara barat daya dan barat)
        elif abs(dy) < abs(dy):
            print('Pem') # lebih ke selatan (antara selatan dan barat daya)
    elif dx < 0 < dy: # dx < 0 and dy > 0 kuadran kiri atas
        if abs(dx) > dy:
            print('Ram') # lebih ke barat (antara barat dan barat laut)
        elif dy > abs(dx):
            print('An') # lebih ke utara (antara barat laut dan utara)
