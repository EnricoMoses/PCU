import numpy as np

a = np.array([1,2,3,4,5])
print(a)

# array 2 D
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(b)

# komponen matriks nol dan satu
o = np.ones([2,3])
z = np.zeros([3,2])
# print(o)
# print(z)
print(b.shape) # ukuran matrix
print(b.ndim) # dimensi matrix
print(b.size) # jumlah elemen
print(b.dtype) # tipe data

print(b[1,2])
print(b[0:2, 1:3])