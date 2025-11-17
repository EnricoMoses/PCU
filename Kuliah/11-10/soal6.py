data = {
    'nama': 'Andi',
    'umur': 21,
    'kota': 'Jakarta'
}

print(data['kota'])

data_2 = {
    'nama': 'Budi',
    'umur': 25,
}

data_2['pekerjaan'] = 'programmer'

print(data_2)

data_3 = {
    'Andi': 85,
    'Budi': 90,
    'Citra': 78
}

rata_rata = sum(data_3.values()) / len(data_3)
print(rata_rata)


