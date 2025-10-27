menu = [
    ['c1', 'Adi', 81],
    ['c2', 'Ani', 87],
    ['c3', 'Surya', 72]
]

n=len(menu)
for i in range(n):
    swapped = False

    for j in range(n-i-1):
        if menu[j][2] < menu[j+1][2]:
            menu[j], menu[j+1] = menu[j+1], menu[j]
            swapped = True
    if not swapped:
        break
# print(menu)

print(*menu, sep='\n')
print(*[f"Nama: {n}\tNRP: {nrp}\tNilai: {v}" for nrp,n,v in menu], sep="\n")
print(*[f'{nrp}, {n}, {v}' for nrp,n,v in menu], sep="\n")
