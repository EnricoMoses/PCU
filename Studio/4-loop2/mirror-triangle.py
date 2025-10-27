n = 4
for i in range(1, n):
    for j in range(i-1):
        print(' ', end='')

    for j in range(i, n+1):
        print(j, end='')
    print()

# for i in range(n):
#     for j in range(n-i-1):
#         print('*', end='')
#     #
#     # for j in range(i+1):
#     #     print(j, end='')
#     for j in range(1, n+1):
#         if j
#         print(j, end='')
#
#     print()

for i in range(n, 0, -1):
    for j in range(1, n+1):
        if j < i:
            print(' ', end='')
        else:
            print(j, end='')
        # print(j, end='')
    print()