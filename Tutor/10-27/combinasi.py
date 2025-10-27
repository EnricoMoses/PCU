def perm(kata, hasil):
    if len(kata) == 0:
        print(hasil)
        return
    for i in range(len(kata)):
        temp = kata[0:i] + kata[i+1::]
        perm(temp, hasil + kata[i])

perm('ABCD', '')

def comb(kata):
    for i in range(2**len(kata)):
        format1 = f"{len(kata):02d}" + 'b'
        biner = format(i, format1)
        temp = ''
        for i in range(len(biner)):
            if biner[i] == '1':
                temp += kata[i]

        print(temp)

comb('ABCD')