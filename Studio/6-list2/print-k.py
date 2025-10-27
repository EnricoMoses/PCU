res = [
    [1, 2],
    [3, 4]
]

for i in range(2):
    print(*res[i])

print(*([[0]*2 for _ in range(2)]))