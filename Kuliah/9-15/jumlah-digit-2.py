bil = int(input())

total = 0
while bil > 0:
    sisa = bil % 10
    total = total + sisa
    bil = bil // 10

print(total)
