def print_pattern(n):
    if n == 0:
        return

    print(n, end='')
    print_pattern(n - 1)
    print(n, end='')

n = int(input())
print_pattern(n)
