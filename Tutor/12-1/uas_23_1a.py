n = int(input())

# minim_3 = total_panjang // 3
# minim_2 = (total_panjang % 3) // 2
# minim_1 = (total_panjang % 2) // 1

piece = [3,2,1]
count = 0
for i in piece:
    count += n // i
    n = n % i

print(count)