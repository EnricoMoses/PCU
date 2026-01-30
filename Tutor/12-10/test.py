def generate(n, current=""):
    if len(current) == n:
        print(current)
        return

    generate(n, current + '0')

    if current == "" or current[-1] != '1':
        generate(n, current + '1')

generate(3)