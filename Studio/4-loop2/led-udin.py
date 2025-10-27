a = int(input())
b = int(input())

for i in range(1, a+1):
    for j in range(b):
        if i % 2 == 0:
            print('#', end=' ')
        else:
            print('*', end=' ')
    print()