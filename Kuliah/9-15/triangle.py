# n = int(input())
# for brs in range(1, n+1):
#     for kol in range(1, 2*brs):
#         print(chr(65+brs-1), end='')
#     print()



n = int(input())
kar = ord('A')
for brs in range(1, n+1):
    for kol in range(1, 2*brs):
        print(chr(kar), end='')
    kar += 1
    if chr(kar) == 'Z':
        kar = 65
    print()
