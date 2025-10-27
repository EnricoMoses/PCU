n = int(input())
if n < 1 or n > 15:
    print(-1)
    exit()

total = 0
temp = 1
if n == 0:
    print(1)
    exit()
else:
    for i in range(1, n+1):
        total = temp * i
        temp = total

print(total)