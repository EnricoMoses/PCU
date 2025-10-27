def is_genap(angka):
    if angka % 2 == 0:
        return True
    return False

my_list = [2,4,7,9,3,0]
total = 0
for i in my_list:
    if is_genap(i):
        total += 1

print(total)
