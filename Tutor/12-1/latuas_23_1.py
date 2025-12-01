n = int(input())
a = list(map(int, input().split()))

index = 1
for i in a:
    if a.count(i) > 1:
        index += 1
    if a.count(i)