# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

def factorial(n):
    if n < 0:
        return 'Erorr'
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


for i in range(10):
    print('0')

print(i)
print(factorial(5))