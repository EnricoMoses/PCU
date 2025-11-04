# def isPowerOfTwo(n):
#     return n > 0 and n & (n - 1)

def isPowerOfTwo(n):
    if n == 1:
        return True


    if n <= 0 or n % 2 != 0:
        return False

    return isPowerOfTwo(n // 2)

n = int(input())
print(isPowerOfTwo(n))