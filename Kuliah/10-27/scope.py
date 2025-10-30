# def my_function():
#     global var # akan membuat var menjadi global
#     var = 2
#     print("Do I know that variable?", var)
#
#
# var = 1
# my_function()
# print(var)

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)
#
#
# var = 1
# my_function(var)
# print(var)

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i

    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))

