derajat = int(input())
is_berawan = int(input())
tekanan_udara = int(input())

if derajat <= 30 and is_berawan == 1 and 1000 <= tekanan_udara <= 1010:
    print('Hujan')
else:
    print('Tidak hujan')
