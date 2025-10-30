# def factorial(angka):
#     if angka == 1:
#         return 1
#     else:
#         return angka * factorial(angka - 1)
#
# print(factorial(5))
def printangka(angka):
    if angka == 0:
        return
    print(angka)
    printangka(angka-1)
    print(angka)


printangka(5)

# arr = [1,1]
# def fibbonaci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if len(arr) == n:
#         return arr[n-1]
#     return fibbonaci(n-1) + fibbonaci(n-2)
#
#
# print(fibbonaci(7))