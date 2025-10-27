n = int(input())
n = str(n)

if '-' in n:
    n.replace('-', '')
    # print('-', end='')
    # for i in range(len(n) -1, -1, -1):
    #     print(n[i], end="")
    print(n)

else :
    for i in range(len(n) -1, -1, -1):
        print(n[i], end="")
